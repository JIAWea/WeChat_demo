"""
Django settings for WeChatPM project.

Generated by 'django-admin startproject' using Django 2.1.8.

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
SECRET_KEY = 'eq#zfs#63fn4y(fohncfz3n69579-4ki=7#(lyrz7934gbg8zn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.apps.BackendConfig',
    'api.apps.ApiConfig'
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

ROOT_URLCONF = 'WeChatPM.urls'

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

WSGI_APPLICATION = 'WeChatPM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'wcpm',
        'USER': 'root',
        'PASSWORD': 'Zopen2013',
        'HOST': '',
        'PORT': '3306',
        'OPTIONS':{
            "init_command":"SET foreign_key_checks = 0;",       # 用于admin后台操作错误
        }
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
AUTH_USER_MODEL = 'backend.BackendUser'                 # 自定制用户登录验证

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = False

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

LOGIN_URL = '/login/'           # 要跳转的下一页的url

# SESSION_COOKIE_AGE = 60 * 30              # 单位是秒
SESSION_SAVE_EVERY_REQUEST = True           # 每次请求都保留session
SESSION_EXPIRE_AT_BROWSER_CLOSE = True      # 关闭浏览器，则COOKIE失效

STATIC_ARTICLE_IMG = os.path.join(BASE_DIR,'static','uploadImgs','article')     # 文章图片上传路径

STATIC_INFO_IMG = os.path.join(BASE_DIR,'static','uploadImgs','infomation')     # 公告图片上传路径

STATIC_REPAIR_IMG = os.path.join(BASE_DIR,'static','uploadImgs','repair')     # 报修图片上传路径

STATIC_CAROUSEL_IMG = os.path.join(BASE_DIR,'static','uploadImgs','carousel')     # 轮播图图片上传路径

USER_UP_XLSX = os.path.join(BASE_DIR,'uploads','xlsx')     # 轮播图图片上传路径