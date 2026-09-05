"""Gera a imagem padrao de compartilhamento (Open Graph) do site.

Saida: theme/static/img/og-default.jpg, em 1200x630 — o tamanho que
Facebook, LinkedIn, WhatsApp, Slack e X esperam.

Uso:
    ./.venv/Scripts/python.exe tools/make_og.py

Rode de novo sempre que mudar o nome, a chamada ou a foto do site.
Requer Pillow, que esta em requirements-dev.txt (nao e preciso no build).
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "theme" / "static" / "img" / "og-default.jpg"
FOTO = RAIZ / "theme" / "static" / "img" / "profile.jpg"

L, A = 1200, 630

# Paleta do tema, identica a de theme/static/css/style.css
FUNDO = (26, 15, 43)
DESTAQUE = (169, 123, 255)
TEXTO = (239, 233, 251)
TEXTO_FRACO = (168, 158, 194)

# Fontes do Windows. Segoe UI e a mais proxima da Public Sans do site.
FONTES = {
    "black": "C:/Windows/Fonts/seguibl.ttf",
    "bold": "C:/Windows/Fonts/segoeuib.ttf",
    "regular": "C:/Windows/Fonts/segoeui.ttf",
}


def fonte(nome: str, tamanho: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(FONTES[nome], tamanho)
    except OSError:
        return ImageFont.load_default(tamanho)


def brilho(img: Image.Image) -> None:
    """Reproduz o gradiente roxo do topo esquerdo do site."""
    camada = Image.new("RGB", (L, A), FUNDO)
    d = ImageDraw.Draw(camada)
    d.ellipse((-260, -420, 900, 480), fill=(64, 38, 104))
    d.ellipse((-120, -300, 520, 260), fill=(88, 52, 140))
    camada = camada.filter(ImageFilter.GaussianBlur(160))
    img.paste(camada, (0, 0))


def avatar(img: Image.Image, tamanho: int, pos: tuple[int, int]) -> None:
    """Cola a foto recortada em circulo, com aro na cor de destaque."""
    if not FOTO.exists():
        return
    foto = Image.open(FOTO).convert("RGB")
    lado = min(foto.size)
    esq = (foto.width - lado) // 2
    topo = (foto.height - lado) // 2
    foto = foto.crop((esq, topo, esq + lado, topo + lado)).resize(
        (tamanho, tamanho), Image.LANCZOS
    )

    mascara = Image.new("L", (tamanho * 4, tamanho * 4), 0)
    ImageDraw.Draw(mascara).ellipse((0, 0, tamanho * 4, tamanho * 4), fill=255)
    mascara = mascara.resize((tamanho, tamanho), Image.LANCZOS)

    aro = ImageDraw.Draw(img)
    aro.ellipse(
        (pos[0] - 5, pos[1] - 5, pos[0] + tamanho + 5, pos[1] + tamanho + 5),
        outline=DESTAQUE,
        width=5,
    )
    img.paste(foto, pos, mascara)


def main() -> None:
    img = Image.new("RGB", (L, A), FUNDO)
    brilho(img)
    d = ImageDraw.Draw(img)

    avatar(img, 150, (84, 96))

    # Ponto + dominio, como no cabecalho do site
    d.ellipse((262, 137, 278, 153), fill=DESTAQUE)
    d.text((292, 128), "rafaelacorrea.dev", font=fonte("regular", 30), fill=(203, 178, 255))

    d.text((84, 300), "Head in the cloud,", font=fonte("black", 76), fill=TEXTO)
    d.text((84, 386), "pés em Belém.", font=fonte("black", 76), fill=TEXTO)

    d.text(
        (84, 500),
        "Rafaela Corrêa · cloud · python · comunidade",
        font=fonte("regular", 30),
        fill=TEXTO_FRACO,
    )

    # Faixa inferior na cor de destaque
    d.rectangle((0, A - 10, L, A), fill=DESTAQUE)

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    img.save(SAIDA, "JPEG", quality=88, optimize=True)
    print(f"gerado: {SAIDA.relative_to(RAIZ)}  ({SAIDA.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
