from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(Union)
admin.site.register(SemiMetroArea)