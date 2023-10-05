from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, MedicalInformation


class CustomUserAdmin(UserAdmin):
    # Customize the admin interface for your user model here
    list_display = ('email', 'name', 'date_of_birth', 'is_staff')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)


class MedicalInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'medical_history', 'family_medical_history', 'medication', 'immunization')
    list_filter = ('user',)  # Add any other fields you want to filter by
    search_fields = ('user__email',)  # Add any other fields you want to search by


# Register the MedicalInformation model with its admin class
admin.site.register(MedicalInformation, MedicalInformationAdmin)
