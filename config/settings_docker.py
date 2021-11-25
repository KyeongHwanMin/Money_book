from config.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '172.17.0.1',
        'PORT': '13306',
    }
}
