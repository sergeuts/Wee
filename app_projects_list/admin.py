from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Users)
admin.site.register(Projects)
#admin.site.register(Purposes)
#admin.site.register(Sources)