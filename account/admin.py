from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser


class UserAdminConfig(UserAdmin):
    model = 'NewUser'

    ordering = ['-date_joined']

    search_fields = ['email', 'first_name', 'last_name']

    list_filter = ['email', 'date_joined', 'is_active', 'is_staff', 'is_superuser']

    list_display = ['__str__', 'email', 'date_joined', 'is_active', 'is_staff']

    list_editable = ['is_active', 'is_staff']

    fieldsets = (
        ('Information', {'fields': ('email', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        ('New User', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
