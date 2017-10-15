from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='b(sx)ez5cca37%)_&p(lv-6)r(8-d+x06_$t19500ij+hf$#tp')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
