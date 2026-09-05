AUTHOR = "Rafaela Correa"
SITENAME = "Rafaela Correa"
SITESUBTITLE = "Notas e artigos"
SITEURL = ""  # vazio = links relativos, correto para o servidor local

PATH = "content"
OUTPUT_PATH = "output"

TIMEZONE = "America/Sao_Paulo"
DEFAULT_LANG = "pt"
LOCALE = ("pt_BR", "Portuguese_Brazil")

# Arquivos estaticos copiados como estao
STATIC_PATHS = ["images", "extra"]

# O arquivo CNAME precisa cair na raiz do site (exigencia do GitHub Pages
# para o dominio proprio). Sem isto ele iria parar em /extra/CNAME.
EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}
ARTICLE_PATHS = [""]
PAGE_PATHS = ["pages"]

# URLs limpas: /meu-artigo/ em vez de /meu-artigo.html
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Feeds desligados no ambiente local (gerar so na publicacao)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = ()
SOCIAL = (("GitHub", "https://github.com/rafaelacorrea"),)

MENUITEMS = (("Sobre", "/pages/sobre/"),)
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

# Recarrega o navegador nao, mas evita cache velho durante o desenvolvimento
DELETE_OUTPUT_DIRECTORY = True
