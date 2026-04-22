DEBUG = True
ALLOWED_HOSTS = ["*"]
STATIC_URL = '/static/'
ROOT_URLCONF = 'todo_project.urls'
SECRET_KEY = 'django-insecure-abc123xyz456yourkey'

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'todo',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # you can add custom template dirs here later
        'APP_DIRS': True,  # IMPORTANT for app templates
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
