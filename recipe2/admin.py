from django.contrib import admin

from recipe2.models import Author, Recipe, Favorites

admin.site.register(Author)
admin.site.register(Recipe)
admin.site.register(Favorites)
