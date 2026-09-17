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
    'django-insecure-r1!ba@*1+cd94^uhlvm)6s*9#q!xd_ni3d+!xe(@n6nh6btuzv'
)

DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'


# ======================================================
# HOSTS PERMITIDOS
# ======================================================

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


# Si Netlify proporciona un dominio mediante variable
NETLIFY_HOST = os.environ.get('NETLIFY_HOST')

if NETLIFY_HOST:
    ALLOWED_HOSTS.append(NETLIFY_HOST)


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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ======================================================
# ARCHIVOS MEDIA
# ======================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# ======================================================
# CONFIGURACIÓN POR DEFECTO
# ======================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
