from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import TutorProfile


class CustomUserAdmin(UserAdmin):
    models = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('More info', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('More info', {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'subjects', 'experience_years')
    search_fields = ('user__username', 'subjects')
    list_filter = ('subjects', 'experience_years')

admin.site.register(TutorProfile, TutorProfileAdmin)