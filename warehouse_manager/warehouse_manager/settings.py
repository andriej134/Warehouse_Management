import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# --------------------------------------
# 1) Dodaj django.contrib.sites i allauth
INSTALLED_APPS = [
    # domyślne Django:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # potrzebne dla allauth:
    'django.contrib.sites',

    # Twoje appki:
    'inventory',

    # allauth:
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # dopisz tu providerów, np.:
    # 'allauth.socialaccount.providers.google',
]
# --------------------------------------

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # allauth middleware (opcjonalne, ale zalecane)
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'warehouse_manager.urls'

# --------------------------------------
# 2) Ustaw TEMPLATES z request context
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # jeżeli masz własny folder globalny: BASE_DIR/'templates'
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',      # <-- konieczne dla allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# --------------------------------------

WSGI_APPLICATION = 'warehouse_manager.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------------------
# 3) Dodaj.backends, by allauth brał udział w auth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',            # Django admin
    'allauth.account.auth_backends.AuthenticationBackend',  # allauth
]
# --------------------------------------

# przekierowania po login/logout
LOGIN_REDIRECT_URL  = '/'
LOGOUT_REDIRECT_URL = '/'

LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_TZ        = True

STATIC_URL        = '/static/'
STATICFILES_DIRS  = [ BASE_DIR / "static" ]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
