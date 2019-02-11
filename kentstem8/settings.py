"""
Django settings for kentstem8 project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q=!okun@6#njlp5)3z13iy5rnvpz29i#aeobx7)#h2orwd&&#w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [ 
    'users.apps.UsersConfig',
    'ndmu.apps.NDMUConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kentstem8',
    'django_filters',
    'ckeditor',
    'ckeditor_uploader',
    'whatsnew',
]

WSGI_APPLICATION = 'kentstem8.wsgi.application'

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'config.image_previewText': '',
        'toolbar': 'Custom',
        'width': 1060,
        'height': 500,
        'extraPlugins': ','.join(['image2', 'justify', 'tableresize',]),        
        'toolbar_Custom': [
            ['Bold', 'Italic','Underline',], ['TextColor', 'BGColor', 'FontSize', 'Font'], ['Link', 'Unlink'],
            ['JustifyBlock', 'JustifyLeft', 'JustifyCenter', 'JustifyRight'], ['NumberedList', 'BulletedList', 'Table'], ['Smiley', 'Image',
            'Outdent', 'Indent', 'Source'], ['Undo', 'Redo', 'Preview', 'Margin', 'lineheight'],
        ],
        'image_previewText': 'Insert Image',
        'smiley_path': '/static/ckeditor smiley/smiley/images/',
        'smiley_images': [
        'regular_smile.png','sad_smile.png','wink_smile.png','teeth_smile.png','confused_smile.png','tongue_smile.png',
        'embarrassed_smile.png','omg_smile.png','whatchutalkingabout_smile.png','angry_smile.png','angel_smile.png','shades_smile.png',
        'devil_smile.png','cry_smile.png','lightbulb.png','thumbs_down.png','thumbs_up.png','heart.png',
        'broken_heart.png','kiss.png','envelope.png', 'ndmu.png', 'embarassed.png', '002-sad-14.png', '003-rich-1.png',
        '004-surprised-1.png', '005-vomit.png', '006-laughing-3.png', '007-angry-4.png', '008-silent.png', '009-surprised.png',
        '010-favorite.png', '011-suspicious.png', '012-sick-3.png', '013-liar.png', '014-dribble.png', '015-laughing-2.png',
        '016-sick-2.png', '017-clown.png', '018-cowboy.png', '019-happy-7.png', '020-robot.png', '021-injured.png', '022-thinking-1.png',
        '023-nerd.png', '024-sick-1.png', '025-rich.png', '026-secret.png', '027-monkey-2.png', '028-monkey-1.png', '029-monkey.png',
        '030-thinking.png', '031-happy-6.png', '032-happy-5.png', '033-sad-13.png', '034-cat-8.png', '035-cat-7.png', '036-cat-6.png',
        '037-cat-5.png', '038-cat-4.png', '039-cat-3.png', '040-cat-2.png', '041-cat-1.png', '042-cat.png', '043-sick.png', '044-muted.png',
        '045-shocked-6.png', '046-sleeping-1.png', '047-embarrassed-3.png', '048-shocked-5.png', '049-shocked-4.png', '050-embarrassed-2.png',
        '051-shocked-3.png', '052-shocked-2.png', '053-crying-2.png', '054-shocked-1.png', '055-sad-12.png', '056-sad-11.png', '057-sad-10.png',
        '058-sad-9.png', '059-sad-8.png', '060-sad-7.png'
        ],
        'smiley_columns': '5',
    },
    'title_editor': {
        'toolbar': 'Title',
        'width': 1060,
        'height': 80,        
        'toolbar_Title': [
        ['Bold', 'Underline', 'TextColor', 'Link', 'Unlink',
        'Undo', 'Redo'],
        ],
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kentstem8.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'ndmu-announcements'
LOGIN_URL = 'login'

