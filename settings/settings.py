from pathlib import Path
import environ, os

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [env("DJANGO_CSRF_TRUSTED_ORIGINS"),]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my apps
    'bot',
    # install app
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
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
]

ROOT_URLCONF = env("DJANGO_ROOT_URLCONF")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = env("DJANGO_WSGI_APPLICATION")


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env("DJANGO_DATABASE_ENGINE"),
        'NAME': BASE_DIR / env("DJANGO_DATABASE_NAME"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = env("DJANGO_LANGUAGE_CODE")
TIME_ZONE = env("DJANGO_TIME_ZONE")
USE_I18N = env("DJANGO_USE_I18N")
USE_TZ = env("DJANGO_USE_TZ")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = env("DJANGO_STATIC_PATH")
STATICFILES_DIRS = [os.path.join(BASE_DIR, STATIC_URL)]
MEDIA_URL = env("DJANGO_MEDIA_PATH")
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = env("DJANGO_DEFAULT_AUTO_FIELD")

# Logger
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{'
        },
        'reports': {
            'format': "{asctime} {levelname} {funcName} {filename}:{lineno} - {message}",
            'style': '{'
        }
    },
    'handlers': {
        "file": {
            "class": "logging.FileHandler",
            "filename": env("LOGGER_FILE"),
            "encoding": "utf-8",
            "formatter": "file",
        },
        "rotating_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": env("LOGGER_FILE"),
            "encoding": "utf-8",
            "formatter": "file",
        },
        "reports": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": env("LOGGER_REPORTS"),
            "formatter": "reports",
        },
    },
    'loggers': {
        "django": {
            "handlers": ["reports"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["file", "rotating_file"],
            "level": "WARNING",
            "propagate": False,
        },
    }
}
