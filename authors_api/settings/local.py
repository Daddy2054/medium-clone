from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
# python -c "import secrets; print(secrets.token_urlsafe(38))"
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="SPi7qWkLBDN4b2Zwa7W0ktCX09Fd5HMqXF2F37FC4epue8T0chY",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
# SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False
# CSRF_COOKIE_SECURE=True
