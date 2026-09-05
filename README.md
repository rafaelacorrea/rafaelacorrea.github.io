# rafaelacorrea.dev

Site e blog pessoal da Rafaela Corrêa — anotações públicas de estudo em AWS,
Python e desenvolvimento mobile, e o que aprendo organizando comunidade de
mulheres na tecnologia.

**No ar:** <https://rafaelacorrea.dev>

Site estático gerado com [Pelican](https://getpelican.com/), conteúdo em
Markdown, tema próprio e publicação automática no GitHub Pages.

## Como rodar localmente

Requer Python 3.12 ou superior.

```bash
git clone git@github.com:rafaelacorrea/rafaelacorrea.github.io.git
cd rafaelacorrea.github.io

python -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.txt   # Windows
# source .venv/bin/activate && pip install -r requirements.txt  # Linux/macOS

./.venv/Scripts/pelican.exe content -s pelicanconf.py -r -l -p 8000
```

Abra <http://localhost:8000>. O `-r` reconstrói o site a cada alteração salva;
basta recarregar a página.

## Como escrever um post

Crie um arquivo `.md` em `content/` com o cabeçalho de metadados no topo:

```markdown
Title: Título do post
Date: 2026-09-04 10:00
Category: aws
Tags: iam, segurança
Slug: titulo-do-post
Summary: Uma frase que aparece na home e na busca.

Texto em Markdown aqui.
```

O campo `Date` é obrigatório — sem ele o Pelican ignora o arquivo em silêncio.

Metadados opcionais reconhecidos pelo tema:

| Campo | Efeito |
| --- | --- |
| `Status: draft` | Não aparece na home; fica só em `/drafts/` |
| `Cover: images/foo.jpg` | Imagem de capa no lugar do padrão listrado |
| `Cover_caption:` | Legenda do bloco de capa quando não há imagem |

Imagens vão em `content/images/` e são referenciadas como
`![legenda]({static}/images/foto.jpg)`.

## Estrutura

```
content/            Posts (.md) e páginas (pages/)
theme/              Tema próprio
  templates/        Jinja2: base, index, article, page, tag, category…
  static/css/       style.css (geral) e pages.css (páginas internas)
  static/img/       Imagens do tema
pelicanconf.py      Configuração de desenvolvimento e textos do tema
publishconf.py      Sobrescreve para produção (domínio, feeds)
.github/workflows/  Build e deploy automáticos
```

Os textos do site — título do hero, cartão "agora", bio, links de redes —
ficam em `pelicanconf.py`, não dentro dos templates. Para mudar a chamada da
home não é preciso abrir HTML.

## Publicação

Todo push na branch `main` dispara o workflow `.github/workflows/pages.yml`,
que gera o site com `publishconf.py` e publica no GitHub Pages. O domínio
próprio vem de `content/extra/CNAME`.

Para gerar o build de produção localmente:

```bash
./.venv/Scripts/pelican.exe content -s publishconf.py
```

## Licença

O código e o tema estão sob a [licença MIT](LICENSE).

O conteúdo editorial — textos dos posts, páginas e imagens de autoria própria —
não está coberto pela MIT. Para reutilizar, entre em contato.
