from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("追加情報", {
            "fields": ("address", "birth_date", "phone", "postal_code")
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
