import os    #requiredforDB
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key")
DEBUG = os.environ.get("DEBUG") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")



# INSTALLED APPS (minimal)
INSTALLED_APPS = [
    'django.contrib.contenttypes',   # required internally
    'django.contrib.staticfiles',    # for static files
    'todo',                          # your app
]

# MIDDLEWARE (minimal)
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

# ROOT URL CONFIG
ROOT_URLCONF = 'todo_project.urls'

# TEMPLATES (required for HTML rendering)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,   # important for app templates
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

# DATABASE 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST', 'db'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# STATIC FILES
STATIC_URL = '/static/'

# DEFAULT FIELD (needed in Django 5+)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
