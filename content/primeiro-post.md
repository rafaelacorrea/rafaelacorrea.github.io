Title: Primeiro post
Date: 2026-09-04 10:00
Category: Geral
Tags: pelican, inicio
Slug: primeiro-post
Summary: O post inicial do blog, gerado com Pelican e servido em localhost.

Este e o primeiro artigo do blog.

## Como escrever um post novo

Crie um arquivo `.md` dentro de `content/` com o cabecalho de metadados
no topo (as linhas `Title:`, `Date:` etc.) e o texto em Markdown abaixo.
O `Date` e obrigatorio; sem ele o Pelican ignora o arquivo.

## Formatacao

Texto em **negrito**, em *italico* e com `codigo inline`.

```python
def ola(nome):
    return f"Ola, {nome}!"
```

- Item de lista
- Outro item

> Citacao em bloco.

[Link para a documentacao do Pelican](https://docs.getpelican.com/)
