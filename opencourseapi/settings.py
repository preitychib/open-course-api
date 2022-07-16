"""
Django settings for opencourseapi project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from environs import Env
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'cloudinary',

    #? Custom apps
    'api',
    'user',
    'image_upload',
    'course',
    'course_section',
    'course_video',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  #? CORS
    'whitenoise.middleware.WhiteNoiseMiddleware',  #? Whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'opencourseapi.urls'

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

WSGI_APPLICATION = 'opencourseapi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600),
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#Password Validators
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.UserModel'

CORS_ALLOW_ALL_ORIGINS = True

# yapf: disable
#? Jazzmin settings
JAZZMIN_SETTINGS = {
    #? title of the window (Will default to current_admin_site.site_title if absent or None)
    'site_title': 'Open Course Ware API Admin',

    #? Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    'site_header': 'Open Course Ware',

    #? Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    'site_brand': 'Open Course Ware',

    #? Logo to use for your site, must be present in static files, used for brand on top left
    # 'site_logo': 'books/img/logo.png',

    #? Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    # 'login_logo': None,

    #? CSS classes that are applied to the logo above
    # 'site_logo_classes': 'img-circle',

    #? Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    # 'site_icon': None,

    #? Welcome text on the login screen
    'welcome_sign': 'Welcome to the Open Course Ware',

    #? Copyright on the footer
    'copyright': 'Open Course Ware',

    #? The model admin to search from the search bar, search bar omitted if excluded
    # 'search_model': 'auth.User',

    #? Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    # 'user_avatar': None,

    ############
    # Top Menu #
    ############

    #? Links to put along the top menu
    'topmenu_links': [

        #? Url that gets reversed (Permissions can be added)
        {
            'name': 'Home',
            'url': 'admin:index',
            'permissions': ['auth.view_user']
        },

        #? model admin to link to (Permissions checked against model)
        {
           # 'model': 'user.User'
            'model': 'auth.User'
        },

        # #? JSON Schema Link
        # {
        #     'name': 'Schema JSON', 'url': '/api/schema/json/', 'new_window': True
        # },

        # #? Swagger Link
        # {
        #     'name': 'Swagger', 'url': '/api/schema/swagger/', 'new_window': True
        # },

        # #? Redoc Link
        # {
        #     'name': 'Redoc', 'url': '/api/schema/redoc/', 'new_window': True
        # },


    ],

    #############
    # Side Menu #
    #############

    #? Whether to display the side menu
    'show_sidebar': True,

    #? Whether to aut expand the menu
    'navigation_expanded': True,

    #? Hide these apps when generating side menu e.g (auth)
    'hide_apps': [],

    #? Hide these models when generating side menu (e.g auth.user)
    'hide_models': [],

    #? List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    'order_with_respect_to': ['auth'],

    #? Custom icons for side menu apps/models
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        # 'user': 'fas fa-user-cog',
         'auth.Group': 'fas fa-users',
        # 'college': 'fas fa-university',
        # 'college.CollegeModel': 'fas fa-university',
    },

    #? Icons that are used when one is not manually specified
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-archive',

    #################
    # Related Modal #
    #################
    #? Use modals instead of popups
    'related_modal_active': False,

    #############
    # UI Tweaks #
    #############
    #? Relative paths to custom CSS/JS scripts (must be present in static files)
    'custom_css': None,
    'custom_js': None,
    #? Whether to show the UI customizer on the sidebar
    'show_ui_builder': False,

    ###############
    # Change view #
    ###############
    #? Render out the change view as a single form, or in tabs, current options are
    #? - single
    #? - horizontal_tabs (default)
    #? - vertical_tabs
    #? - collapsible
    #? - carousel
    'changeform_format': 'horizontal_tabs',
}

JAZZMIN_UI_TWEAKS={
    'footer_small_text': False,
    'body_small_text': False,
    'brand_small_text': False,
    'brand_colour': False,
    'accent': 'accent-primary',
    'navbar': 'navbar-white navbar-light',
    'no_navbar_border': False,
    'navbar_fixed': True,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': True,
    'sidebar': 'sidebar-light-primary',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': False,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': False,
    'theme': 'default',
    # 'dark_mode_theme': None,
    'button_classes': {
        'primary': 'btn-outline-primary',
        'secondary': 'btn-outline-secondary',
        'info': 'btn-outline-info',
        'warning': 'btn-outline-warning',
        'danger': 'btn-outline-danger',
        'success': 'btn-outline-success'
    },
    'actions_sticky_top': True
}

# yapf: enable

#? DRF Config
REST_FRAMEWORK = {
    #? Authentication Config
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework_simplejwt.authentication.JWTAuthentication',
     'rest_framework.authentication.SessionAuthentication',
     'rest_framework.authentication.BasicAuthentication'),

    #? DRF Schema Class
    'DEFAULT_SCHEMA_CLASS':
    'drf_spectacular.openapi.AutoSchema',

    # #TODO: Permisions
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),

    #TODO: Pagination Config
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 10,

    #TODO: Filters Config
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    # ),

    #TODO: API Throttling Config
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ),
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '1000/day',
    #     'user': '1000/day'
    # },

    #TODO: Versioning related Config
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # 'DEFAULT_VERSION': '1.0',
    # 'ALLOWED_VERSIONS': ('1.0',),
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
}

#? Spectacular Config
SPECTACULAR_SETTINGS = {
    'TITLE': 'Open Course Ware API',
    'DESCRIPTION': 'API for Open Course Ware',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': True,
        'displayRequestDuration': True,
        'filter': True,
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
            '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/opencourseware.log',
            'formatter': 'verbose',
            'backupCount': 5,
            'maxBytes': 10485760,  #? 10 MB
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

#? max request size check
DATA_UPLOAD_MAX_MEMORY_SIZE = None

#? Cloudinary Config
cloudinary.config(
    cloud_name=env.str('CLOUDINARY_CLOUD_NAME'),
    api_key=env.str('CLOUDINARY_API_KEY'),
    api_secret=env.str('CLOUDINARY_API_SECRET'),
    secure=True,
)
