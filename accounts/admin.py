from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Account

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superadmin",
        "last_login",
    )
    list_display_links = ("email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff", "is_superadmin")
    fieldsets = ()
    readonly_fields = ('last_login','date_joined')
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(Account, CustomUserAdmin)
