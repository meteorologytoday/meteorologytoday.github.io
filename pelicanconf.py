SITE_INFO = dict(
    AUTHOR = "Tien Tien",
    EMAIL = "tienyiao@ucsd.edu",
    TITLE = "Personal Website",
)

AUTHOR = 'XTT'
SITENAME = 'Tien-Yiao Hsu Personal Website'
SITEURL = "localhost:8000/"

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
ARTICLE_PATHS = ['posts']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%Y%m%d}_{slug}.html'
ARTICLE_URL = '/{date:%Y}/{date:%Y%m%d}_{slug}.html'

MENUITEMS = (
  ('About', '/'),
  ('Notes', '/pages/notes'),
  ('Posts', '/categories'),
  ('Links', '/pages/links'),
)

STATIC_PATHS = ['static']

DEFAULT_PAGINATION = 10

THEME = "theme"
LOAD_CONTENT_CACHE = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
