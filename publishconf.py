# Config de PUBLICACAO. Herda tudo de pelicanconf.py e sobrescreve o necessario.
# Uso: pelican content -s publishconf.py
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F403

SITEURL = "https://rafaelacorrea.dev"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

# Analytics do Plausible (self-hosted). Fica so aqui de proposito: builds
# locais com pelicanconf.py nao carregam o script e nao poluem as metricas.
PLAUSIBLE_SRC = "https://devsnorte-plausible.fly.dev/js/pa-gKUKjoVP2RtbDSVcv6dD0.js"

DELETE_OUTPUT_DIRECTORY = True
