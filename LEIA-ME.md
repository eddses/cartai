# Site + QR code da Cartaí: como colocar no ar

São 3 passos, uns 10 minutos, tudo grátis.

## 1. Contador de acessos (GoatCounter)
1. Entre em **https://www.goatcounter.com/signup**.
2. Em *Code*, coloque **`cartai`**. O painel vai ficar em `https://cartai.goatcounter.com`.
   - Se `cartai` já estiver em uso, escolha outro (ex.: `cartaioficial`). Depois, abra o `index.html`, procure `cartai.goatcounter.com` (está no fim do arquivo) e troque pelo seu código.
3. Confirme o e-mail e pronto: o painel mostra as visitas por dia, o país, o celular ou computador e **quantas vieram pelo QR** (aparecem com a origem `qr`).

## 2. Publicar o site (GitHub Pages)
O site fica no repositório `eddses/cartai`, publicado pelo GitHub Pages em
**https://eddses.github.io/cartai/**. Cada alteração enviada ao repositório atualiza o site em 1 ou 2 minutos.

## 3. QR code
- O `qr/qr-cartai.png` já aponta para **`https://eddses.github.io/cartai/?utm_source=qr`**.
- **Só gere de novo se o endereço do site for diferente**:
  ```
  pip install segno pillow
  python3 qr/gerar_qr.py https://SEU-ENDERECO
  ```
  (Ou é só me mandar o endereço que eu gero.)
- `qr-cartai.png`: tem 1800 px e o sol no meio; serve para slides, posts e impressão.
- `qr-cartai.svg`: é vetor, sem o sol, e é o ideal para mandar para a gráfica.
- Imprima com pelo menos **2,5 cm** de lado.

> **Importante:** teste o QR com o celular **depois** que o site estiver no ar. Ele aponta para o endereço do site; se o site não estiver publicado com esse nome, o QR abre uma página de erro.
