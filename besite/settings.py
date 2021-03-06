##################################################################
FileName		= 'settings.py'
# By:			Jason Thorne
# Date:			11-03-2012
# Description: 	The built project
##################################################################
# For checking if running on development or production site
import os
from math import pi
#  Django settings for besite project.

# r144 earths average radius in meters from Wikipedia, and radians <=> degrees
EARTHRADIUS			= 6371000
DEG2RAD				= pi/180.0
RAD2DEG				= 180.0/pi
# r166
# The server does not check for compulsory fields on registration OTHER THAN EMAIL
# this is to allow V1 of the application to work. V2 of the app does not allow the
# user to register unless they enter all the compulsory fields.
# THE FIRST COMPULSORY FIELD MUST BE 'email'
COMPULSORY_REGISTRATION_FIELDS 	= ['email', 'first_name', 'gender', 'birth_year']
#COMPULSORY_REGISTRATION_PROMPTS	= ['Email', 'First Name', 'Gender (F, M)', 'Year of Birth']
COMPULSORY_REGISTRATION_PROMPTS 	= ['email', 'first_name', 'gender', 'birth_year']
OPTIONAL_REGISTRATION_FIELDS 	= ['organisation',  'suburb', 'residentYears']
#OPTIONAL_REGISTRATION_PROMPTS	= ['Organisation', 'Suburb', 'Years Residence']
OPTIONAL_REGISTRATION_PROMPTS 	= ['organisation',  'suburb', 'residentYears']
# the minimum age for registration
MINIMUM_AGE						= 13

# r180
# constant for enumerated list
GENDERTYPE			= ( \
	('M', 'Male'), 
	('F', 'Female'),
)
male				= 0
female				= 1

# r 158 If this is being run as jason, then turn debugging on
if "USER" in os.environ:
	if os.environ['USER'] == 'jason':
		DEBUG				= True
	else:
		DEBUG 				= False
	# end if 
else:
	DEBUG 				= False
# end if

TEMPLATE_DEBUG = DEBUG
PDFDEBUG = DEBUG

ADMINS = (
    ('Jason Thorne', 'jthorne@magiclamp.com.au'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'built',                      # Or path to database file if using sqlite3.
        'USER': 'built',                      # Not used with sqlite3.
        'PASSWORD': 'built',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Sydney'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT 			= '/www/built/besite/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL 			= 'http://liveable.eng.unsw.edu.au/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
# ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/www/built/besite/env_issues/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'at%=hz!#s&ox0n-(85a^kmz!4gsnlq(q5pi*c$3w_6ve6dvej1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # The line below is used for security. It does not encrypt, but makes sure the
    # posting/getting client uses an identification key. Anyhow, without understanding
    # it properly, leaving it on makes posting forms impossible.
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'besite.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	'/www/built/betemplates/'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
	'polls',
	# stands for environmental issues
	'env_issues', 
	'api_wikki',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# r179
#  use gmail for sending emails
EMAIL_HOST			= 'SMTP.GMAIL.COM'
EMAIL_PORT			= '587'
EMAIL_HOST_USER	= 'lokiWebmaster@gmail.com'
EMAIL_HOST_PASSWORD = 'sivaraman'
EMAIL_USE_TLS		= True