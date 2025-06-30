from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-dummy-key-for-dev"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "sample_project",
    "django.contrib.staticfiles",
    "django_cosmograph",  # Use your package here
]

MIDDLEWARE = []

ROOT_URLCONF = "sample_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Optional custom templates
        "APP_DIRS": True,
        "OPTIONS": {},
    },
]

WSGI_APPLICATION = "sample_project.wsgi.application"

STATIC_URL = "/static/"
STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
