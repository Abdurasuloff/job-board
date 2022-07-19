from django.contrib import admin
from .models import Category, Vacancy, Apply

# Register your models here.
admin.site.register(Category)
admin.site.register(Vacancy)
admin.site.register(Apply)