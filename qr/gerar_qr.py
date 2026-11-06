"""Gera o QR code da Cartaí nas cores da marca.

Uso:
    python3 gerar_qr.py https://SEU-SITE

O QR aponta para o endereço com ?utm_source=qr, para o contador separar
quem entrou pelo QR de quem entrou por outro caminho.
Gera qr-cartai.png (para tela/impressão) e qr-cartai.svg (para gráfica).
"""
import sys, os
import segno
from PIL import Image, ImageDraw

VINHO = "#590e0f"
CREME = "#fbefdc"
AQUI = os.path.dirname(os.path.abspath(__file__))

base = (sys.argv[1] if len(sys.argv) > 1 else "https://eddses.github.io/cartai").rstrip("/")
url = f"{base}/?utm_source=qr"

qr = segno.make(url, error="h")  # correção alta: aguenta o sol no meio
qr.save(os.path.join(AQUI, "qr-cartai.svg"), scale=10, border=4, dark=VINHO, light=CREME)

png = os.path.join(AQUI, "qr-cartai.png")
qr.save(png, scale=40, border=4, dark=VINHO, light=CREME)

# sol da marca no centro, numa caixa alinhada aos módulos do QR
# (correção H aguenta até ~30% de área coberta; aqui cobrimos bem menos)
img = Image.open(png).convert("RGBA")
W = img.width
mod = 40
n = qr.symbol_size(scale=1, border=0)[0]
lado = 9 if n >= 37 else 7          # caixa de 9x9 módulos
ini = (4 + (n - lado) // 2) * mod
caixa = Image.new("RGBA", (lado * mod, lado * mod), (0, 0, 0, 0))
ImageDraw.Draw(caixa).rounded_rectangle([0, 0, lado * mod - 1, lado * mod - 1], radius=mod, fill=CREME)
sol = Image.open(os.path.join(AQUI, "..", "img", "sol.webp")).convert("RGBA")
sol.thumbnail((int(lado * mod * 0.8), int(lado * mod * 0.8)), Image.LANCZOS)
caixa.alpha_composite(sol, ((caixa.width - sol.width) // 2, (caixa.height - sol.height) // 2))
img.alpha_composite(caixa, (ini, ini))
img.convert("RGB").save(png, dpi=(300, 300))

print("QR gerado para:", url)
print(" ->", png)
print(" ->", os.path.join(AQUI, "qr-cartai.svg"), "(sem o sol; ideal para a gráfica)")
