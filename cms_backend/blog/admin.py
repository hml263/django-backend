from django.contrib import admin

from .models import Blog

admin.site.site_header = 'Avete' 
admin.site.register(Blog)