from .base import *

#nuestra base de datos local

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if config('DEBUG') == 'True':
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	    }
	}
else:
	DATABASES = {
    'default': {
        'ENGINE': config('ENGINE'),
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': '',
    }
}
