from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'dev-secret-key-123'   # change in production
DEBUG = True
ALLOWED_HOSTS = ["*"]   # for Docker / EC2

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

# DATABASE (dummy, Django expects it)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dummy.sqlite3',
    }
}

# STATIC FILES
STATIC_URL = '/static/'

# DEFAULT FIELD (needed in Django 5+)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
