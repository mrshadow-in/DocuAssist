from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# from medgpt.users.models import CustomUser, MedicalInformation
from .forms import UserForm, MedicalInformationForm


@login_required
def my_profile(request):
    user = request.user
    return render(request, 'my.html', {'user': user})


@login_required
def edit_my_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    else:
        form = UserForm(instance=user)
    return render(request, 'my_edit.html', {'user': user, 'form': form})


@login_required
def medical_information(request):
    user = request.user
    medical_info = user.medical_info
    return render(request, 'medinfoview.html', {'user': user, 'medical_info': medical_info})


@login_required
def edit_medical_information(request):
    user = request.user
    if request.method == 'POST':
        form = MedicalInformationForm(request.POST, instance=user.medical_info)
        if form.is_valid():
            form.save()
            return redirect('medical_information')
    else:
        form = MedicalInformationForm(instance=user.medical_info)
    return render(request, 'medinfo_edit.html', {'user': user, 'form': form})


@login_required
def my_reports(request):
    user = request.user
    reports = user.diagnostic_reports.all()
    return render(request, 'myreports.html', {'user': user, 'reports': reports})


from django.shortcuts import render

# Create your views here.
