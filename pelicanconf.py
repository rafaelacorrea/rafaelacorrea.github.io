AUTHOR = "Rafaela Corrêa"
SITENAME = "Rafaela Corrêa"
SITESUBTITLE = "Anotações públicas de estudo em AWS, Python e desenvolvimento mobile."
SITEURL = ""  # vazio = links relativos, correto para o servidor local

PATH = "content"
OUTPUT_PATH = "output"
THEME = "theme"

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
CATEGORY_URL = "categoria/{slug}/"
CATEGORY_SAVE_AS = "categoria/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
ARCHIVES_SAVE_AS = "arquivo/index.html"

# So estas paginas avulsas sao geradas (dispensa templates tags/categories/authors)
DIRECT_TEMPLATES = ["index", "archives"]

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Feeds desligados no ambiente local (gerados so na publicacao)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# ---------------------------------------------------------------------------
# Conteudo do tema. Fica aqui, e nao dentro dos templates, para poder ser
# editado sem mexer em HTML.
# ---------------------------------------------------------------------------

SITE_BRAND = "rafaelacorrea.dev"
SITE_LOCATION = "Belém, PA"
COPYRIGHT_YEAR = 2026

NAVLINKS = [
    ("posts", "/"),
    ("projetos", "/pages/projetos/"),
    ("sobre", "/pages/sobre/"),
    ("cv", "/pages/curriculo/"),
    ("contato", "/pages/contato/"),
]

HERO_NAME = "rafaela corrêa"
HERO_TAGLINE = "cloud · python · comunidade"
HERO_TITLE = "Head in the cloud,<br>pés em Belém."
HERO_LEDE = (
    "Anotações públicas de estudo em AWS, Python e desenvolvimento mobile "
    "— e o que aprendo organizando comunidade de mulheres na tecnologia."
)

NOW_ITEMS = [
    {"img": "pyladies.jpg", "role": "Coordenadora de comunidade", "org": "PyLadies Belém"},
    {"img": "elas-na-tech.jpg", "role": "Coordenadora de comunidade", "org": "Elas na Tecnologia"},
    {"img": "escola-da-nuvem.jpg", "role": "Aprendiz de Cloud", "org": "Escola da Nuvem · AWS"},
]

AUTHOR_BIO = (
    "Coordenadora de comunidade na PyLadies Belém e Elas na Tecnologia. "
    "Aprendiz de cloud na Escola da Nuvem."
)

SOCIAL_GITHUB = "https://github.com/rafaelacorrea"
SOCIAL_LINKEDIN = "https://www.linkedin.com/in/rafaelafccorrea/"
SOCIAL_INSTAGRAM = "https://instagram.com/rafaelacorrea"
SOCIAL_EMAIL = "oi@rafaelacorrea.dev"

# Buy Me a Coffee. Preencha BMC_USERNAME com o nome de usuario da conta
# (o trecho final de buymeacoffee.com/SEU-USUARIO) para o botao aparecer no
# fim dos posts e no rodape. Vazio = nada e exibido.
BMC_USERNAME = ""
BMC_LABEL = "Me pague um café"
BMC_TITLE = "Gostou do post?"
BMC_TEXT = (
    "Escrevo essas anotações no tempo livre. Se algo aqui te ajudou, "
    "um café ajuda a manter o caderno aberto."
)

# O formulario do design nao tem servico por tras ainda; desligado ate ter um.
NEWSLETTER_ENABLED = False
NEWSLETTER_TITLE = "Newsletter quinzenal"
NEWSLETTER_SUB = "Um resumo do que estudei em cloud e dos próximos encontros em Belém."
NEWSLETTER_ACTION = ""

LINKS = ()
SOCIAL = ()
