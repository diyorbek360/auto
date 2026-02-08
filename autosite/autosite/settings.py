from pathlib import Path
import os

# Корень проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Статика
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'catalog' / 'static',  # если есть дополнительные CSS/JS
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Медиа
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Безопасность
SECRET_KEY = 'django-insecure-u&wc*ks(g5e+k41#1tbjhq_gm&7ohoc)j0#ke3)u#99^pg15nm'
DEBUG = True
ALLOWED_HOSTS = []

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',
    'rest_framework',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL конфиг
ROOT_URLCONF = 'autosite.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # глобальные папки шаблонов, можно добавить позже
        'APP_DIRS': True,  # искать templates/ внутри приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'autosite.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Остальное
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
