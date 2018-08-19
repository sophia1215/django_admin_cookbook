from django.contrib import admin

from .models import Category, Hero, Villain, Origin

# Register your models here.
admin.site.register(Category)
admin.site.register(Hero)
admin.site.register(Villain)
admin.site.register(Origin)

