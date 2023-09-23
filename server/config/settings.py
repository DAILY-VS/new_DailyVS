import os, environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / '../.env')

SECRET_KEY=env('SECRET_KEY')


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

MYSQL_DBNAME=env('MYSQL_DBNAME')
MYSQL_USERNAME=env('MYSQL_USERNAME')
MYSQL_PASSWD=env('MYSQL_PASSWD')
MYSQL_HOST=env('MYSQL_HOST')
MYSQL_PORT=env('MYSQL_PORT')

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DBNAME,
        'USER': MYSQL_USERNAME,
        'PASSWORD': MYSQL_PASSWD,
        'HOST': MYSQL_HOST,
        'PORT': MYSQL_PORT,
    }
}
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "vs_account",
    "vote",
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',

    "rest_framework", #추가 코드
    "corsheaders", # cors 추가 코드
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',     # 추가
    'django.middleware.common.CommonMiddleware', # 추가
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware', #
    'django.contrib.auth.middleware.RemoteUserMiddleware', #
    'allauth.account.middleware.AccountMiddleware',
]

# CORS 추가
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8000', 'http://localhost:3000')
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = "config.urls"
SOCIALACCOUNT_LOGIN_ON_GET = True
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False

AUTH_USER_MODEL = "vs_account.User"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

FAVICON_PATH = os.path.join(BASE_DIR, "static", "favicon.ico")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',    
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '6e0b76c3ceeb04bed80541df1eb81445',
            'secret': '7GHqOVkfQnvOf81TcIxtk91JW2VceNnJ',
            'key': ''
        }
    }
}

LOGIN_REDIRECT_URL = '/'   # social login redirect
ACCOUNT_LOGOUT_REDIRECT_URL = 'https://daily-vs.com/accounts/kakao/login/callback/'
AUTH_USER_MODEL = "vs_account.User"  ##


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=env('EMAIL_PORT')
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER

SITE_ID = 1 