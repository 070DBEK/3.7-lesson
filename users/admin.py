from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'date_of_birth', 'gender', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('gender', 'is_staff', 'is_active')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'date_of_birth', 'gender')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'gender', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(User, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_level', 'goal', 'height', 'weight')
    search_fields = ('user__username', 'user__email')
    list_filter = ('activity_level',)

admin.site.register(UserProfile, UserProfileAdmin)
