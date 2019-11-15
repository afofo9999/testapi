from django.contrib import admin
from .models import category, movie, actor



admin.site.register(movie)
admin.site.register(actor)
admin.site.register(category)

