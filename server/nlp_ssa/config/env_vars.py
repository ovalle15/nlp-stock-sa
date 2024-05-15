import os


GITHUB_OAUTH_CLIENT_ID = os.getenv("GITHUB_OAUTH_CLIENT_ID", default="")
GITHUB_OAUTH_CLIENT_SECRET = os.getenv("GITHUB_OAUTH_CLIENT_SECRET", default="")
GITHUB_OAUTH_CALLBACK_URL = os.getenv("GITHUB_OAUTH_CALLBACK_URL", default="")
GITHUB_OAUTH_SCOPES = []


CSRF_SECRET = (os.getenv("CSRF_SECRET", "TMP"),)
DATABASE_USER = (os.getenv("DATABASE_USER", "postgres"),)
DATABASE_PASSWORD = (os.getenv("DATABASE_PASSWORD", "example"),)
DATABASE_HOST = (os.getenv("DATABASE_HOST", "database"),)
DATABASE_PORT = (os.getenv("DATABASE_PORT", "5432"),)
DATABASE_NAME = (os.getenv("DATABASE_NAME", "the_money_maker"),)
ENV = (os.getenv("ENV", "dev"),)
LOG_LEVEL = (os.getenv("LOG_LEVEL", "DEBUG"),)
LOG_SQL = (os.getenv("LOG_SQL", False),)
