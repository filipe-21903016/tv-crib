from django.contrib import admin
from .models import Show, Character, Category, CastMember

# Register your models here.
admin.site.register(Character)
admin.site.register(Category)
admin.site.register(CastMember)
admin.site.register(Show)

