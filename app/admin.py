from django.contrib import admin

from app.models import Article, UserProfile

admin.site.register(UserProfile)
admin.site.register(Article)
