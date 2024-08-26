
import os

from pathlib import Path
from channels.auth import AuthMiddlewareStack
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = 'myapp.MyAppUser'
SESSION_COOKIE_AGE = 36000

SECRET_KEY = os.getenv('SECRET_KEY')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
DJANGO_ALLOW_ASYNC_UNSAFE = True
SIGNING_KEY = os.environ.get("JWT_SECRET_KEY")

if os.environ.get('DEBUG') in ['1', 'true']:
    DEBUG = True

PBKDF2_ITERATIONS = 180000  # Number of iterations (default is 180,000)
PBKDF2_SALT_LENGTH = 12     # Length of generated salt (default is 12)
PBKDF2_DIGEST = 'sha256'
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',  # Default PBKDF2 algorithm
    'django.contrib.auth.hashers.Argon2PasswordHasher',  # Argon2 algorithm (recommended for newer projects)
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',  # BCrypt algorithm with SHA-256 hash
]

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'myapp',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'SIGNING_KEY': SIGNING_KEY, 
    'ALGORITHM': 'HS256',
    'VERIFY_EXPIRATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ACCESS_TOKEN_LIFETIME': timedelta(days=60),

}

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'
ASGI_APPLICATION = 'myproject.routing.application'
INTERACTIVE = False


CHANNEL_LAYERS = {
     'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer', 
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER', 'user'),
        'PASSWORD': os.environ.get('PGPASSWORD', 'password'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}


X_FRAME_OPTIONS = 'ALLOWALL'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        
    ),
}




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CSRF_TRUSTED_ORIGINS = [
    'http://localhost',
    'https://localhost',
    'http://localhost:8443',
    'https://localhost:8443',
    'https://localhost:443',
    'http://127.0.0.1',
    'https://127.0.0.1:8000',
    'https://127.0.0.1',
    'https://api.intra.42.fr',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost',
    'https://localhost',
    'http://localhost:8443',
    'https://localhost:8443',
    'https://localhost:443',
    'http://127.0.0.1',
    'https://127.0.0.1:8000',
    'https://127.0.0.1',
    'https://api.intra.42.fr',
]

CORS_ORIGIN_ALLOW_ALL = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_COOKIE_SECURE = False
APPEND_SLASH=False

