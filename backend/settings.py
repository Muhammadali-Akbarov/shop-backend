"""
Django settings for backend project.
"""

from pathlib import Path
from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

SECRET_KEY = \
    "django-insecure-t#@*2$mqaow1igr(+v2j76)7-d9fojetpv)#c3oz@ce*x+(y%)"

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "unfold",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'payme',
    'click_up',

    'order',
    'payment',
]

PAYTECH_LICENSE_API_KEY = "d8806bbf-0c01-4cd4-a347-27caf7858ff2" # you can get your api key from https://docs.pay-tech.uz/console

# payme settings
PAYME_ID = env.str("PAYME_ID")
PAYME_KEY = env.str("PAYME_KEY")
PAYME_ACCOUNT_FIELD = "id"  # maybe id key
PAYME_AMOUNT_FIELD = "total_cost"
PAYME_ACCOUNT_MODEL = "order.models.Order"
PAYME_ONE_TIME_PAYMENT = True

# click settings
CLICK_SERVICE_ID = env.str("CLICK_SERVICE_ID")
CLICK_MERCHANT_ID = env.str("CLICK_MERCHANT_ID")
CLICK_SECRET_KEY = env.str("CLICK_SECRET_KEY")
CLICK_ACCOUNT_MODEL = "order.models.Order"
CLICK_AMOUNT_FIELD = "total_cost"

# CLICK_COMMISSION_PERCENT = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", # noqa
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
