import os

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    contact = models.CharField(max_length=20)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=20)
    otp = models.CharField(max_length=6, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth', 'gender', 'address', 'contact', 'emergency_contact_name',
                       'emergency_contact_number']

    def __str__(self):
        return self.email


class MedicalInformation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='medical_info')
    medical_history = models.TextField(null=True, blank=True)
    family_medical_history = models.TextField(null=True, blank=True)
    medication = models.TextField(null=True, blank=True)
    immunization = models.TextField(null=True, blank=True)
    lifestyle_factor = models.TextField(null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    past_hospitalization = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')], null=True,)
    surgical_history = models.TextField(null=True, blank=True)
    social_history = models.TextField(null=True, blank=True)
    mental_health_history = models.TextField(null=True, blank=True)
    gynological_disorder = models.TextField(null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.email


def user_report_upload_path(instance, filename):
    # Get the user's name
    user_name = instance.user.name
    # Clean the filename to remove special characters and spaces
    filename = os.path.basename(filename)
    # Combine the user's name and cleaned filename to generate the path
    return f'diagnostic_reports/{user_name}/{filename}'


class DiagnosticReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='diagnostic_reports')
    report_file = models.FileField(upload_to=user_report_upload_path, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Diagnostic Report for {self.user.email} ({self.uploaded_at})"
