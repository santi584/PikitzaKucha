
from pathlib import Path
import os


# ======================================================
# RUTAS DEL PROYECTO
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ======================================================
# CONFIGURACIÓN BÁSICA
# ======================================================

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'local-development-secret-key-pikitza-kucha-2026-8fK3mP9xL2vR7qW5'
)

DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() == 'true'


# ======================================================
# HOSTS PERMITIDOS
# ======================================================

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

# Dominio proporcionado automáticamente por Render
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Compatibilidad con la configuración anterior
NETLIFY_HOST = os.environ.get('NETLIFY_HOST')

if NETLIFY_HOST:
    ALLOWED_HOSTS.append(NETLIFY_HOST)


# ======================================================
# SEGURIDAD PARA PRODUCCIÓN
# ======================================================

SECURE_SSL_REDIRECT = not DEBUG

# Render termina HTTPS en su proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_SECURE = not DEBUG

CSRF_COOKIE_SECURE = not DEBUG

if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    if RENDER_EXTERNAL_HOSTNAME:
        CSRF_TRUSTED_ORIGINS = [
            f'https://{RENDER_EXTERNAL_HOSTNAME}'
        ]


# ======================================================
# APLICACIONES INSTALADAS
# ======================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Nuestra aplicación
    'web',
]


# ======================================================
# MIDDLEWARE
# ======================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ======================================================
# URLS
# ======================================================

ROOT_URLCONF = 'pikitza.urls'


# ======================================================
# TEMPLATES
# ======================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ======================================================
# WSGI
# ======================================================

WSGI_APPLICATION = 'pikitza.wsgi.application'


# ======================================================
# BASE DE DATOS
# ======================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ======================================================
# VALIDADORES DE CONTRASEÑAS
# ======================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ======================================================
# IDIOMA Y ZONA HORARIA
# ======================================================

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_TZ = True


# ======================================================
# ARCHIVOS ESTÁTICOS
# ======================================================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}


# ======================================================
# ARCHIVOS MEDIA
# ======================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# ======================================================
# CONFIGURACIÓN POR DEFECTO
# ======================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
