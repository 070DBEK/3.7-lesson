from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'gender'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'gender', 'date_of_birth', 'is_staff')
    list_filter = ('gender', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'activity_level', 'goal')
    list_filter = ('activity_level', 'goal')
    search_fields = ('user__username', 'user__email')
