from django.contrib import admin
from .models import Photo, User, People
admin.site.register(User)
admin.site.register(Photo)
admin.site.register(People)
