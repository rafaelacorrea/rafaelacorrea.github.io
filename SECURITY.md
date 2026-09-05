# Política de Segurança

## Escopo

Este repositório contém um site estático publicado no GitHub Pages. Ele não
tem backend, banco de dados, autenticação nem processa dados de pessoas
visitantes — o que reduz bastante a superfície de ataque.

Ainda assim, são relevantes:

- Vulnerabilidades nas dependências de build (`requirements.txt`)
- Problemas no workflow do GitHub Actions (`.github/workflows/`)
- Conteúdo capaz de executar script indevidamente no navegador de quem visita
- Configuração incorreta de domínio, DNS ou HTTPS

## Versões suportadas

Apenas o conteúdo publicado a partir da branch `main`, que corresponde ao que
está no ar em <https://rafaelacorrea.dev>.

## Como reportar

**Não abra uma issue pública** para falhas de segurança.

Prefira o canal privado do GitHub: aba **Security → Report a vulnerability**
deste repositório (GitHub Private Vulnerability Reporting).

Alternativamente, envie e-mail para **oi@rafaelacorrea.dev** com:

- Descrição do problema e do impacto
- Passos para reproduzir
- Versão, navegador ou ambiente, quando fizer diferença

## O que esperar

- **Confirmação de recebimento:** até 5 dias úteis
- **Retorno com avaliação inicial:** até 15 dias úteis
- Você será creditada na correção, se quiser

Como este é um projeto pessoal mantido por uma pessoa só, não há programa de
recompensa (*bug bounty*).

## Por favor, não

- Não execute testes que degradem o serviço, como negação de serviço ou
  varreduras automatizadas em volume
- Não acesse, altere ou exponha dados de terceiros
- Não divulgue publicamente a falha antes de ela ser corrigida
