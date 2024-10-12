# Seletor de skins para Kingdom Two Crowns

Este seletor é um utilitário pessoal feito em Python, que serve para trocar a skin do jogador do Kingdom Two Crowns, já que o jogo não suporta esse tipo de edição in-game. A skin pode ser alterada tanto para o jogador 1, quanto para o jogador 2.

O script foi desenvolvido levando em consideração o local de instalação default do jogo através da Steam. Por mais que ele suporte sistemas Linux, Windows e MacOS, ele foi testado apenas em Linux e MacOS. Portanto, caso você tente executar este script e ele não encontre os arquivos do jogo, tente alterar a localização para sua preferência.

Esse utilitário foi escrito com base nos arquivos do jogo Kingdom Two Crowns, porém nada impede dele ser modificado para os outros jogos da franquia. A estrutura de todos eles é bem similar, e as informações podem ser facilmente mapeadas através da wiki da série.

## Como utilizar

### Requisitos

Para poder utilizar o script, basta ter os seguintes requisitos:

- Python 3
- Instalação de Kingdom Two Crowns
- Save válido de Kingdom Two Crowns

### Antes de executar

- Certifique-se que o caminho do save está correto dentro do script.
- Faça um backup do seu save atual.

### Para executar

Para executar, basta utilizar o comando python abaixo:

```
python3 skin_selector.py
```