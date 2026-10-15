#!/usr/bin/env python3
"""
Monta un vídeo de diapositivas narrado (MP4 1080p, H.264 + AAC) a partir de un deck.md.

    deck.md -> PNG por diapositiva (Pillow) -> voz por diapositiva -> MP4 (ffmpeg)

Voz, por orden de preferencia en cada diapositiva:
  1. `audio: ruta` en el deck (la voz que aporta el usuario: grabada, ElevenLabs, la que sea)
  2. edge-tts, SOLO si ya está instalado (gratis; no se instala desde aquí)
  3. sin voz: la diapositiva dura lo que diga `duration:` o `--seconds-per-slide`

Probado en Linux y en Windows; pensado también para Mac (busca las fuentes Arial de macOS).
Requisitos: Python 3.9+, Pillow, ffmpeg y ffprobe.

Uso:
    python build_video.py deck.md -o salida.mp4
    python build_video.py deck.md -o salida.mp4 --accent 8b5cf6 --no-motion --srt
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError:
    sys.exit("ERROR: falta Pillow. Instálalo con: python -m pip install pillow")


# --------------------------------------------------------------------------- temas

THEMES: dict[str, dict[str, str]] = {
    # Sobrio por defecto: gris carbón, texto casi blanco, acento neutro.
    "sobrio": {"bg": "#121417", "fg": "#F4F4F5", "muted": "#A1A1AA", "accent": "#D4D4D8"},
    "claro": {"bg": "#FAFAFA", "fg": "#18181B", "muted": "#52525B", "accent": "#18181B"},
    "noche": {"bg": "#0B1220", "fg": "#E5E7EB", "muted": "#94A3B8", "accent": "#60A5FA"},
}

HEX_RE = re.compile(r"^#?([0-9a-fA-F]{6})$")


def parse_hex(value: str, name: str) -> tuple[int, int, int]:
    m = HEX_RE.match(value.strip())
    if not m:
        raise ValueError(f"el color '{name}' no es un hex de 6 cifras: {value!r} (ejemplo: 8b5cf6)")
    h = m.group(1)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


# --------------------------------------------------------------------------- deck

@dataclass
class Slide:
    kind: str  # "title" | "section" | "content"
    heading: str
    subtitle: str = ""
    body: list[str] = field(default_factory=list)
    bullets: list[str] = field(default_factory=list)
    narration: list[str] = field(default_factory=list)
    image: Path | None = None
    audio: Path | None = None
    duration: float | None = None
    line: int = 0  # línea del deck donde empieza, para los mensajes de error

    @property
    def narration_text(self) -> str:
        return " ".join(t.strip() for t in self.narration if t.strip())


BULLET_RE = re.compile(r"^\s*(?:[-*]|・)\s+(.*)$")
NARR_RE = re.compile(r"^\s*(?:>\s?|(?:narration|narración|vo)\s*:\s*)(.*)$", re.IGNORECASE)
KEY_RE = re.compile(r"^\s*(image|imagen|audio|duration|duracion|duración)\s*:\s*(.+)$", re.IGNORECASE)
COMMENT_RE = re.compile(r"^(.*?)\s+#.*$")


def _strip_value(raw: str) -> str:
    """Quita comentarios `  # ...` (con espacio delante, para no romper los hex) y comillas."""
    v = raw.strip()
    m = COMMENT_RE.match(v)
    if m and not v.startswith("#"):
        v = m.group(1).strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v


def parse_deck(path: Path) -> tuple[dict[str, str], list[Slide]]:
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    lines = text.splitlines()

    meta: dict[str, str] = {}
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            ln = lines[i]
            if ":" in ln and not ln.lstrip().startswith("#"):
                k, v = ln.split(":", 1)
                meta[k.strip().lower()] = _strip_value(v)
            i += 1
        if i >= len(lines):
            raise ValueError("el frontmatter empieza con '---' pero no se cierra con otro '---'")
        i += 1

    slides: list[Slide] = []
    base = path.parent
    seen_title = False
    current: Slide | None = None

    for n in range(i, len(lines)):
        raw = lines[n]
        s = raw.strip()
        lineno = n + 1
        if not s:
            continue
        if s.startswith("## "):
            current = Slide(kind="content", heading=s[3:].strip(), line=lineno)
            slides.append(current)
            continue
        if s.startswith("# "):
            kind = "section" if seen_title else "title"
            seen_title = True
            current = Slide(kind=kind, heading=s[2:].strip(), line=lineno)
            slides.append(current)
            continue
        if current is None:
            raise ValueError(
                f"línea {lineno}: hay contenido antes de la primera diapositiva. "
                "Empieza con '# Título' o '## Diapositiva'."
            )
        km = KEY_RE.match(s)
        if km:
            key, val = km.group(1).lower(), _strip_value(km.group(2))
            if key in ("image", "imagen"):
                current.image = (base / val).expanduser()
            elif key == "audio":
                current.audio = (base / val).expanduser()
            else:
                try:
                    current.duration = float(val.replace(",", "."))
                except ValueError:
                    raise ValueError(f"línea {lineno}: 'duration' tiene que ser un número de segundos, no {val!r}")
            continue
        nm = NARR_RE.match(s)
        if nm:
            current.narration.append(nm.group(1))
            continue
        bm = BULLET_RE.match(raw)
        if bm:
            current.bullets.append(bm.group(1).strip())
            continue
        # Línea normal: subtítulo bajo un '#', texto bajo un '##'.
        if current.kind in ("title", "section") and not current.subtitle:
            current.subtitle = s
        else:
            current.body.append(s)

    if not slides:
        raise ValueError("el deck no tiene ninguna diapositiva ('# ' o '## ')")
    for sl in slides:
        for label, p in (("image", sl.image), ("audio", sl.audio)):
            if p is not None and not p.is_file():
                raise ValueError(f"línea {sl.line} ('{sl.heading}'): no existe el fichero de {label}: {p}")
    return meta, slides


# --------------------------------------------------------------------------- fuentes

def _font_candidates(bold: bool) -> list[Path]:
    win = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    if bold:
        names = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
            str(win / "segoeuib.ttf"),
            str(win / "arialbd.ttf"),
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/Library/Fonts/Arial Bold.ttf",
        ]
    else:
        names = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/TTF/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
            str(win / "segoeui.ttf"),
            str(win / "arial.ttf"),
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/Library/Fonts/Arial.ttf",
        ]
    return [Path(n) for n in names]


class Fonts:
    def __init__(self, regular: str | None, bold: str | None):
        self.regular_path = self._pick(regular, bold=False)
        self.bold_path = self._pick(bold, bold=True) or self.regular_path
        if self.regular_path is None:
            print(
                "AVISO: no encuentro DejaVu, Segoe UI ni Arial. Uso la fuente interna de Pillow; "
                "pasa --font con una .ttf para mejor resultado.",
                file=sys.stderr,
            )
        self._cache: dict[tuple[bool, int], object] = {}

    @staticmethod
    def _pick(explicit: str | None, bold: bool) -> Path | None:
        if explicit:
            p = Path(explicit).expanduser()
            if not p.is_file():
                raise ValueError(f"no existe la fuente indicada: {p}")
            return p
        for c in _font_candidates(bold):
            if c.is_file():
                return c
        return None

    def get(self, size: int, bold: bool = False):
        key = (bold, size)
        if key not in self._cache:
            path = self.bold_path if bold else self.regular_path
            if path is None:
                self._cache[key] = ImageFont.load_default(size=size)
            else:
                self._cache[key] = ImageFont.truetype(str(path), size)
        return self._cache[key]


# --------------------------------------------------------------------------- dibujo

def wrap(text: str, font, max_w: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if font.getlength(trial) <= max_w:
            cur = trial
            continue
        if cur:
            lines.append(cur)
        # Palabra más ancha que la caja: se parte por caracteres.
        if font.getlength(w) > max_w:
            chunk = ""
            for ch in w:
                if font.getlength(chunk + ch) > max_w and chunk:
                    lines.append(chunk)
                    chunk = ch
                else:
                    chunk += ch
            cur = chunk
        else:
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def line_h(font) -> int:
    asc, desc = font.getmetrics()
    return asc + desc


class Renderer:
    def __init__(self, width: int, height: int, colors: dict[str, tuple[int, int, int]], fonts: Fonts, footer: str):
        self.W, self.H = width, height
        self.c = colors
        self.f = fonts
        self.footer = footer
        self.mx = int(width * 0.08)
        self.my = int(height * 0.10)
        self.warnings: list[str] = []

    def _base(self):
        img = Image.new("RGB", (self.W, self.H), self.c["bg"])
        return img, ImageDraw.Draw(img)

    def _footer(self, d, idx: int, total: int, show_number: bool):
        size = max(18, int(self.H * 0.022))
        font = self.f.get(size)
        y = self.H - int(self.H * 0.05) - line_h(font)
        if self.footer:
            d.text((self.mx, y), self.footer, font=font, fill=self.c["muted"])
        if show_number:
            label = f"{idx} / {total}"
            d.text((self.W - self.mx - font.getlength(label), y), label, font=font, fill=self.c["muted"])

    def _image_box(self, img, path: Path, box: tuple[int, int, int, int]):
        x0, y0, x1, y1 = box
        try:
            pic = Image.open(path)
            pic = ImageOps.exif_transpose(pic).convert("RGBA")
        except Exception as e:  # noqa: BLE001 - se informa del fichero concreto
            raise ValueError(f"no puedo abrir la imagen {path}: {e}") from e
        pic = ImageOps.contain(pic, (x1 - x0, y1 - y0), Image.Resampling.LANCZOS)
        px = x0 + ((x1 - x0) - pic.width) // 2
        py = y0 + ((y1 - y0) - pic.height) // 2
        img.paste(pic, (px, py), pic)

    def render(self, sl: Slide, idx: int, total: int, out: Path):
        img, d = self._base()
        text_right = self.W - self.mx
        if sl.image is not None:
            text_right = int(self.W * 0.56)
            self._image_box(img, sl.image, (int(self.W * 0.60), self.my, self.W - self.mx, self.H - self.my - int(self.H * 0.06)))
        max_w = text_right - self.mx

        if sl.kind in ("title", "section"):
            self._render_title(d, sl, max_w, big=(sl.kind == "title"))
            self._footer(d, idx, total, show_number=(sl.kind == "section"))
        else:
            self._render_content(d, sl, max_w, idx)
            self._footer(d, idx, total, show_number=True)
        img.save(out, "PNG")

    def _render_title(self, d, sl: Slide, max_w: int, big: bool):
        h_size = int(self.H * (0.095 if big else 0.080))
        s_size = int(self.H * 0.042)
        min_h = int(self.H * 0.05)
        while True:
            hf = self.f.get(h_size, bold=True)
            h_lines = wrap(sl.heading, hf, max_w)
            if len(h_lines) <= 3 or h_size <= min_h:
                break
            h_size -= 4
        sf = self.f.get(s_size)
        s_lines = wrap(sl.subtitle, sf, max_w) if sl.subtitle else []
        bar_h = max(6, int(self.H * 0.008))
        gap = int(self.H * 0.03)
        total_h = bar_h + gap + len(h_lines) * int(line_h(hf) * 1.05)
        if s_lines:
            total_h += gap + len(s_lines) * int(line_h(sf) * 1.15)
        y = (self.H - total_h) // 2
        d.rectangle([self.mx, y, self.mx + int(self.W * 0.06), y + bar_h], fill=self.c["accent"])
        y += bar_h + gap
        for ln in h_lines:
            d.text((self.mx, y), ln, font=hf, fill=self.c["fg"])
            y += int(line_h(hf) * 1.05)
        if s_lines:
            y += gap
            for ln in s_lines:
                d.text((self.mx, y), ln, font=sf, fill=self.c["muted"])
                y += int(line_h(sf) * 1.15)

    def _layout_content(self, sl: Slide, max_w: int, h_size: int, b_size: int):
        hf = self.f.get(h_size, bold=True)
        bf = self.f.get(b_size)
        pf = self.f.get(b_size)
        h_lines = wrap(sl.heading, hf, max_w)
        indent = int(b_size * 1.3)
        body = [wrap(p, pf, max_w) for p in sl.body]
        bullets = [wrap(b, bf, max_w - indent) for b in sl.bullets]
        height = len(h_lines) * int(line_h(hf) * 1.05) + int(self.H * 0.05)
        for p in body:
            height += len(p) * int(line_h(pf) * 1.2) + int(self.H * 0.02)
        for b in bullets:
            height += len(b) * int(line_h(bf) * 1.2) + int(self.H * 0.028)
        return hf, bf, pf, h_lines, body, bullets, indent, height

    def _render_content(self, d, sl: Slide, max_w: int, idx: int):
        h_size = int(self.H * 0.070)
        b_size = int(self.H * 0.046)
        avail = self.H - 2 * self.my - int(self.H * 0.05)
        min_b = max(24, int(self.H * 0.028))
        while True:
            hf, bf, pf, h_lines, body, bullets, indent, height = self._layout_content(sl, max_w, h_size, b_size)
            if height <= avail or b_size <= min_b:
                break
            b_size -= 2
            h_size = max(int(self.H * 0.05), h_size - 2)
        if height > avail:
            self.warnings.append(
                f"diapositiva {idx} ('{sl.heading}'): el texto no cabe ni al tamaño mínimo. "
                "Quita viñetas o acórtalas (máximo 4, unas 8 palabras cada una)."
            )
        if len(sl.bullets) > 4:
            self.warnings.append(f"diapositiva {idx} ('{sl.heading}'): {len(sl.bullets)} viñetas; el oficio dice 4 como máximo.")

        y = self.my
        for ln in h_lines:
            d.text((self.mx, y), ln, font=hf, fill=self.c["fg"])
            y += int(line_h(hf) * 1.05)
        y += int(self.H * 0.012)
        d.rectangle([self.mx, y, self.mx + int(self.W * 0.05), y + max(4, int(self.H * 0.005))], fill=self.c["accent"])
        y += int(self.H * 0.038)
        for para in body:
            for ln in para:
                d.text((self.mx, y), ln, font=pf, fill=self.c["muted"])
                y += int(line_h(pf) * 1.2)
            y += int(self.H * 0.02)
        dot = max(8, int(b_size * 0.28))
        for b in bullets:
            asc, _ = bf.getmetrics()
            cy = y + int(asc * 0.62)
            d.ellipse([self.mx, cy - dot // 2, self.mx + dot, cy + dot // 2], fill=self.c["accent"])
            for ln in b:
                d.text((self.mx + indent, y), ln, font=bf, fill=self.c["fg"])
                y += int(line_h(bf) * 1.2)
            y += int(self.H * 0.028)


# --------------------------------------------------------------------------- ffmpeg

class Tools:
    def __init__(self, ffmpeg: str | None):
        self.ffmpeg = self._find(ffmpeg or os.environ.get("FFMPEG"), "ffmpeg")
        sibling = Path(self.ffmpeg).with_name("ffprobe" + Path(self.ffmpeg).suffix)
        self.ffprobe = str(sibling) if sibling.is_file() else self._find(None, "ffprobe")

    @staticmethod
    def _find(explicit: str | None, name: str) -> str:
        if explicit:
            if Path(explicit).is_file():
                return explicit
            raise RuntimeError(f"no existe el ejecutable indicado para {name}: {explicit}")
        found = shutil.which(name)
        if not found:
            raise RuntimeError(
                f"no encuentro {name} en el PATH. Instálalo (Windows: winget install Gyan.FFmpeg; "
                "Mac: brew install ffmpeg; Linux: apt install ffmpeg) o pásalo con --ffmpeg."
            )
        return found

    def run(self, args: list[str], what: str):
        proc = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if proc.returncode != 0:
            tail = "\n".join(proc.stderr.strip().splitlines()[-15:])
            raise RuntimeError(f"ffmpeg falló al {what}:\n{tail}")

    def duration(self, path: Path) -> float:
        proc = subprocess.run(
            [self.ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if proc.returncode != 0:
            raise RuntimeError(f"ffprobe no puede leer {path}: {proc.stderr.strip()[-300:]}")
        try:
            return float(json.loads(proc.stdout)["format"]["duration"])
        except (KeyError, ValueError, json.JSONDecodeError) as e:
            raise RuntimeError(f"ffprobe no devuelve duración para {path}") from e


def edge_tts_available() -> bool:
    try:
        import edge_tts  # noqa: F401
    except ImportError:
        return False
    return True


def synth_edge(text: str, voice: str, rate: str, out: Path):
    import edge_tts

    async def _go():
        await edge_tts.Communicate(text, voice, rate=rate).save(str(out))

    try:
        asyncio.run(_go())
    except Exception as e:  # noqa: BLE001 - edge-tts depende de red; se explica el fallo
        raise RuntimeError(f"edge-tts no ha podido generar la voz ({voice}): {e}") from e


def encode_segment(tools: Tools, png: Path, audio: Path | None, dur: float, fps: int,
                   W: int, H: int, motion: bool, out: Path):
    frames = max(1, round(dur * fps))
    if motion:
        vf = (
            f"[0:v]scale={W * 2}:{H * 2},"
            f"zoompan=z='1+0.04*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
            f":d=1:s={W}x{H}:fps={fps},format=yuv420p[v]"
        )
    else:
        vf = f"[0:v]scale={W}:{H},format=yuv420p[v]"
    fade_st = max(0.0, dur - 0.06)
    af = (
        "[1:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,apad,"
        f"afade=t=out:st={fade_st:.3f}:d=0.06[a]"
    )
    args = [tools.ffmpeg, "-y", "-hide_banner", "-loglevel", "error",
            "-loop", "1", "-framerate", str(fps), "-i", str(png)]
    if audio is not None:
        args += ["-i", str(audio)]
    else:
        args += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
    args += ["-filter_complex", f"{vf};{af}", "-map", "[v]", "-map", "[a]",
             "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(fps),
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
             "-t", f"{dur:.3f}", str(out)]
    tools.run(args, f"montar la diapositiva {png.stem}")


def concat(tools: Tools, segments: list[Path], out: Path, work: Path):
    lst = work / "lista.txt"
    with lst.open("w", encoding="utf-8") as fh:
        for seg in segments:
            p = seg.resolve().as_posix().replace("'", "'\\''")
            fh.write(f"file '{p}'\n")
    tools.run([tools.ffmpeg, "-y", "-hide_banner", "-loglevel", "error",
               "-f", "concat", "-safe", "0", "-i", str(lst),
               "-c", "copy", "-movflags", "+faststart", str(out)], "unir las diapositivas")


# --------------------------------------------------------------------------- subtítulos

def srt_time(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def split_cues(text: str, max_chars: int = 84) -> list[str]:
    sentences = re.split(r"(?<=[.!?…])\s+", text.strip())
    cues: list[str] = []
    for sen in sentences:
        cur = ""
        for w in sen.split():
            trial = f"{cur} {w}".strip()
            if len(trial) > max_chars and cur:
                cues.append(cur)
                cur = w
            else:
                cur = trial
        if cur:
            cues.append(cur)
    return cues


def write_srt(path: Path, timeline: list[tuple[float, float, str]]):
    n = 0
    blocks: list[str] = []
    for start, span, text in timeline:
        cues = split_cues(text)
        if not cues:
            continue
        total = sum(len(c) for c in cues)
        t = start
        for c in cues:
            dt = span * len(c) / total
            n += 1
            blocks.append(f"{n}\n{srt_time(t)} --> {srt_time(t + dt)}\n{c}\n")
            t += dt
    path.write_text("\n".join(blocks), encoding="utf-8")


# --------------------------------------------------------------------------- main

def truthy(v: str | None) -> bool | None:
    if v is None:
        return None
    return v.strip().lower() in ("1", "true", "si", "sí", "yes", "on")


def main() -> int:
    ap = argparse.ArgumentParser(description="Vídeo de diapositivas narrado desde un deck.md")
    ap.add_argument("deck", help="ruta al deck.md")
    ap.add_argument("-o", "--output", help="MP4 de salida (por defecto, junto al deck con su nombre)")
    ap.add_argument("--theme", help=f"tema base: {', '.join(sorted(THEMES))} (por defecto: sobrio)")
    ap.add_argument("--bg", help="color de fondo en hex (marca)")
    ap.add_argument("--fg", help="color del texto en hex (marca)")
    ap.add_argument("--muted", help="color del texto secundario en hex (marca)")
    ap.add_argument("--accent", help="color de acento en hex (marca), p. ej. 8b5cf6")
    ap.add_argument("--tts", choices=["auto", "edge", "none"],
                    help="voz sintética: auto (edge-tts si está instalado), edge (obligatorio) o none")
    ap.add_argument("--voice", help="voz de edge-tts (por defecto es-ES-AlvaroNeural)")
    ap.add_argument("--rate", default="+0%", help="velocidad de edge-tts, p. ej. -5%% o +10%%")
    ap.add_argument("--no-audio", action="store_true", help="sin voz: todas las diapositivas con tiempo fijo")
    ap.add_argument("--seconds-per-slide", type=float, help="duración de una diapositiva sin voz (por defecto 5)")
    ap.add_argument("--padding", type=float, default=0.7, help="segundos de aire tras la voz de cada diapositiva")
    ap.add_argument("--no-motion", action="store_true", help="sin el zoom lento sobre cada diapositiva")
    ap.add_argument("--resolution", help="ancho x alto, por defecto 1920x1080 (1080x1920 para vertical)")
    ap.add_argument("--fps", type=int, help="fotogramas por segundo (por defecto 30)")
    ap.add_argument("--footer", help="texto pequeño abajo a la izquierda (marca, web)")
    ap.add_argument("--font", help="fuente .ttf normal")
    ap.add_argument("--font-bold", help="fuente .ttf negrita")
    ap.add_argument("--ffmpeg", help="ruta a ffmpeg si no está en el PATH")
    ap.add_argument("--srt", action="store_true", help="escribe también los subtítulos .srt de la narración")
    ap.add_argument("--keep-temp", action="store_true", help="no borra la carpeta temporal (PNG y segmentos)")
    a = ap.parse_args()

    deck = Path(a.deck).expanduser().resolve()
    if not deck.is_file():
        print(f"ERROR: no existe el deck: {deck}", file=sys.stderr)
        return 2
    try:
        meta, slides = parse_deck(deck)
    except ValueError as e:
        print(f"ERROR en el deck: {e}", file=sys.stderr)
        return 2

    theme_name = (a.theme or meta.get("theme") or "sobrio").strip().lower()
    if theme_name not in THEMES:
        print(f"AVISO: tema desconocido '{theme_name}', uso 'sobrio'. Temas: {', '.join(sorted(THEMES))}", file=sys.stderr)
        theme_name = "sobrio"
    theme = THEMES[theme_name]
    try:
        colors = {}
        for key in ("bg", "fg", "muted", "accent"):
            value = getattr(a, key) or meta.get(key) or theme[key]
            colors[key] = parse_hex(value, key)
        res = a.resolution or meta.get("resolution", "1920x1080")
        m = re.match(r"^\s*(\d+)\s*[xX]\s*(\d+)\s*$", res)
        if not m:
            raise ValueError(f"resolución no válida: {res!r} (ejemplo: 1920x1080)")
        W, H = int(m.group(1)), int(m.group(2))
        if W % 2 or H % 2:
            raise ValueError("la resolución tiene que ser de números pares (H.264)")
        fps = a.fps or int(meta.get("fps", 30))
        sps = a.seconds_per_slide or float(str(meta.get("seconds", 5)).replace(",", "."))
        fonts = Fonts(a.font or meta.get("font"), a.font_bold or meta.get("font_bold"))
        tools = Tools(a.ffmpeg)
    except (ValueError, RuntimeError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    motion = not a.no_motion and truthy(meta.get("motion")) is not False
    tts_mode = "none" if a.no_audio else (a.tts or meta.get("tts", "auto")).strip().lower()
    if tts_mode not in ("auto", "edge", "none"):
        print(f"ERROR: tts '{tts_mode}' no válido (auto, edge o none)", file=sys.stderr)
        return 2
    voice = a.voice or meta.get("voice") or "auto"
    if voice == "auto":
        voice = "es-ES-AlvaroNeural"
    has_edge = edge_tts_available()
    if tts_mode == "edge" and not has_edge:
        print("ERROR: se ha pedido edge-tts pero no está instalado (python -m pip install edge-tts).", file=sys.stderr)
        return 2

    out = Path(a.output).expanduser().resolve() if a.output else deck.with_suffix(".mp4")
    out.parent.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="diapositivas_"))
    renderer = Renderer(W, H, colors, fonts, a.footer or meta.get("footer", ""))
    segments: list[Path] = []
    timeline: list[tuple[float, float, str]] = []
    report: list[str] = []
    silent_with_text: list[int] = []
    t = 0.0

    try:
        total = len(slides)
        for idx, sl in enumerate(slides, start=1):
            png = work / f"d{idx:03d}.png"
            renderer.render(sl, idx, total, png)

            audio: Path | None = None
            source = "sin voz"
            if not a.no_audio and sl.audio is not None:
                audio, source = sl.audio, "audio del deck"
            elif sl.narration_text and tts_mode in ("auto", "edge") and has_edge:
                audio = work / f"d{idx:03d}.mp3"
                synth_edge(sl.narration_text, voice, a.rate, audio)
                source = f"edge-tts ({voice})"
            elif sl.narration_text and not a.no_audio:
                silent_with_text.append(idx)

            if audio is not None:
                voice_len = tools.duration(audio)
                dur = voice_len + a.padding
                if sl.duration is not None:
                    dur = max(dur, sl.duration)
            else:
                voice_len = 0.0
                dur = sl.duration if sl.duration is not None else sps
            dur = max(dur, 1.5)

            seg = work / f"d{idx:03d}.mp4"
            encode_segment(tools, png, audio, dur, fps, W, H, motion, seg)
            segments.append(seg)
            if sl.narration_text:
                span = voice_len if voice_len > 0 else max(1.0, dur - 0.3)
                timeline.append((t, span, sl.narration_text))
            report.append(f"  {idx:>2}. {sl.kind:<8} {dur:5.1f} s  {source:<22} {sl.heading[:50]}")
            t += dur

        concat(tools, segments, out, work)
        if a.srt:
            write_srt(out.with_suffix(".srt"), timeline)
    except (RuntimeError, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        if not a.keep_temp:
            shutil.rmtree(work, ignore_errors=True)
        return 1

    print(f"Vídeo: {out}")
    print(f"Duración total: {t:.1f} s · {len(slides)} diapositivas · {W}x{H} a {fps} fps · movimiento {'sí' if motion else 'no'}")
    print("\n".join(report))
    if a.srt:
        print(f"Subtítulos: {out.with_suffix('.srt')}")
    for w in renderer.warnings:
        print(f"AVISO: {w}", file=sys.stderr)
    if silent_with_text:
        print(
            "AVISO: estas diapositivas tienen narración escrita pero salen sin voz "
            f"(no hay audio ni edge-tts): {', '.join(map(str, silent_with_text))}",
            file=sys.stderr,
        )
    if a.keep_temp:
        print(f"Temporales: {work}")
    else:
        shutil.rmtree(work, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
