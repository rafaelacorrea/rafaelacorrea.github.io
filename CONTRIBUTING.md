# Como contribuir

Obrigada pelo interesse! Este é um site pessoal, então o escopo do que faz
sentido contribuir é um pouco diferente do de um projeto de software comum.

## O que é bem-vindo

- **Correções de conteúdo** — erro de digitação, link quebrado, informação
  desatualizada ou tecnicamente incorreta em um post
- **Correções no site** — problema de layout, de acessibilidade ou de
  comportamento em algum navegador ou tamanho de tela
- **Melhorias no tema** — desde que mantenham a identidade visual atual

## O que provavelmente não será aceito

- Reescrita de textos, mudança de opinião ou de estilo de escrita dos posts:
  o conteúdo editorial é pessoal
- Posts novos escritos por terceiros
- Trocas de tecnologia de fundo (outro gerador de site, outro framework de CSS)
  sem conversa prévia em uma issue

## Antes de abrir um pull request

Para qualquer mudança que não seja trivial, **abra uma issue primeiro**. Evita
que você invista tempo em algo que não vai ser incorporado.

Correções pequenas e óbvias — um typo, um link quebrado — podem ir direto em
um pull request, sem issue.

## Rodando o projeto

O passo a passo está no [README](README.md#como-rodar-localmente). Resumo:

```bash
python -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.txt
./.venv/Scripts/pelican.exe content -s pelicanconf.py -r -l -p 8000
```

## Antes de enviar

- Rode o build e confirme que ele termina sem erro:
  `./.venv/Scripts/pelican.exe content -s publishconf.py`
- Confira a alteração no navegador, inclusive em tela estreita — o tema tem
  pontos de quebra em 860px e 620px
- Mantenha as mensagens de commit curtas e no imperativo, em português
  (ex.: `Corrige link quebrado no post sobre IAM`)
- Um assunto por pull request

## Código de conduta

A participação neste projeto está sujeita ao
[Código de Conduta](CODE_OF_CONDUCT.md).
