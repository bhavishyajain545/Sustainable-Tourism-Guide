import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 SECURITY WARNING: Keep the secret key secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "default-secret-key")  # Use env variable

# ⚠️ SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# 🌍 Allowed Hosts
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    os.getenv("PRODUCTION_HOST", "your-production-domain.com"),
]

# 🔒 CSRF Trusted Origins (Needed for HTTPS)
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    os.getenv("FRONTEND_URL", "https://your-production-domain.com"),
]

# 🛠️ Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # API Framework & Security
    "rest_framework",
    "corsheaders",  # Allow Vue.js frontend to communicate
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Enable CORS
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 🌍 Allow CORS (Frontend Communication)
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True  # Enable for local testing
else:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:8080",  # Vue.js frontend
        os.getenv("FRONTEND_URL", "https://your-production-domain.com"),
    ]

# 🔗 URL Configuration
ROOT_URLCONF = "backend.urls"

# 🏗️ Templates Configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Custom Templates Folder
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

# 🚀 WSGI Application
WSGI_APPLICATION = "backend.wsgi.application"

# 📦 Database Configuration (PostgreSQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sustainable_tourism",
        "USER": "postgres",
        "PASSWORD": "arihant",
        "HOST": "localhost",
        "PORT": "5432",
    }
}



# 🔐 Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🌍 Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 📂 Static Files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 🔑 Default Primary Key Field Type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
