from django import forms
from users.models import CustomUser, MedicalInformation


class MedicalInformationForm(forms.ModelForm):
    class Meta:
        model = MedicalInformation
        fields = '__all__'  # You can specify the fields you want to include here


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['name', 'date_of_birth', 'gender', 'address', 'contact', 'email', 'emergency_contact_name',
                  'emergency_contact_number', 'password']
