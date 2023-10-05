import random

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser, MedicalInformation, DiagnosticReport
from .forms import DiagnosticReportForm


class CustomLoginView(LoginView):
    template_name = 'login.html'


# @login_required(login_url='login')
# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'registration.html')


def regcomplete(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        emergency_contact_name = request.POST['emergency_contact_name']
        emergency_contact_number = request.POST['emergency_contact_number']
        password = request.POST['password']

        # Create the user with email and password
        my_user = CustomUser.objects.create_user(email=email, password=password)
        request.session['registration_email'] = email  # Store the email in the session
        # Set additional fields for the user
        my_user.name = name
        my_user.gender = gender
        my_user.date_of_birth = dob
        my_user.address = address
        my_user.contact = contact
        my_user.emergency_contact_name = emergency_contact_name
        my_user.emergency_contact_number = emergency_contact_number
        otp = ''.join(random.choice('0123456789') for _ in range(6))
        my_user.otp = otp
        my_user.save()
        subject = '[XITE MAILING SYSTEM] OTP for DocuAssist registration'
        message = f'Your OTP for registration on {get_current_site(request)} is {otp}.'
        from_email = 'docuassit@xitegroup.online'  # Update with your email
        recipient_list = [my_user.email]
        send_mail(subject, message, from_email, recipient_list)

        messages.success(request, 'Registration successful. Please verify your email address.')
        return redirect('otp-verify')  # Redirect to a success page

    return HttpResponse('Error!')


from django.contrib.auth import login, logout


# ...

def otp_verify(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        print(entered_otp)
        email = request.session.get('registration_email')  # Get the email stored in the session

        if email:
            print(email)
            user = CustomUser.objects.filter(email=email).first()

            if user and entered_otp == user.otp:
                print("OTP verified")
                # OTP is valid, complete the registration process
                user.otp = None  # Clear the OTP field
                user.save()

                # Log in the user temporarily for OTP verification
                login(request, user)

                # Redirect to the login page
                return redirect('login')
            else:
                print("OTP not verified")
                messages.error(request, 'Invalid OTP. Please try again.')
        else:
            print("Email not found in session")
            messages.error(request, 'Email not found in session. Please register again.')

    return render(request, 'otp_verify.html')


@login_required(login_url='login')
def success(request):
    return render(request, 'regcomplete.html')


@login_required(login_url='login')
def medinfo(request):
    return render(request, 'medinfo.html')


@login_required(login_url='login')
def medcomplete(request):
    if request.method == 'POST':
        # Create and save a MedicalInformation instance
        medical_info = MedicalInformation(
            user=request.user,
            medical_history=request.POST['medical_history'],
            family_medical_history=request.POST['family_medical_history'],
            medication=request.POST['medication'],
            immunization=request.POST['immunization'],
            lifestyle_factor=request.POST['lifestyle_factor'],
            allergies=request.POST['allergies'],
            past_hospitalization=request.POST['past_hospitalization'],
            surgical_history=request.POST['surgical_history'],
            social_history=request.POST['social_history'],
            mental_health_history=request.POST['mental_health_history'],
            gynological_disorder=request.POST['gynological_disorder'],
            additional_information=request.POST['additional_information'],
        )
        medical_info.save()
        return redirect('medsuccess')  # Redirect to a success page

    return HttpResponse('Error!')


@login_required(login_url='login')
def medsuccess(request):
    return render(request, 'medcomplete.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']  # Change 'username' to 'email'
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)  # Change 'username' to 'email'
        if user is not None:
            login(request, user)
            if MedicalInformation.objects.filter(user=user).exists():
                return redirect('medsuccess')  # Redirect to 'success' if medical information is already filled
            else:
                return redirect(
                    'medinfo')  # Redirect to 'medinfo' if medical information is not filled  # Redirect to the
                # 'success' page after successful login
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def upload_diagnostic_report(request):
    if request.method == 'POST':
        form = DiagnosticReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            form.save()
            messages.success(request, 'Diagnostic report uploaded successfully.')
            return redirect('upload_success')  # Redirect to a success page
        else:
            messages.error(request, 'Error uploading diagnostic report. Please check the file format and try again.')
    else:
        form = DiagnosticReportForm()
    return render(request, 'upload.html', {'form': form})


@login_required(login_url='login')
def upload_success(request):
    user = request.user
    report_exists = DiagnosticReport.objects.filter(user=user).exists()
    return render(request, 'upload_success.html', {'report_exists': report_exists})


@login_required(login_url='login')
def myuploads(request):
    # Get the user's diagnostic reports
    user = request.user  # Assuming the user is logged in
    reports = DiagnosticReport.objects.filter(user=user)

    return render(request, 'myuploads.html', {'reports': reports})


def otp_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = CustomUser.objects.filter(email=email).first()

        if user:
            request.session['registration_email2'] = email  # Store the email in the session
            # Generate OTP
            otp = ''.join(random.choice('0123456789') for _ in range(6))
            user.otp = otp
            user.save()

            # Send OTP to user's email
            subject = '[XITE MAILING SYSTEM] OTP for DocuAssist login'
            message = f'Your OTP for DocuAssist login is: {otp}'
            from_email = 'docuassit@xitegroup.online'  # Update with your email
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('otp-verify2')  # Redirect to OTP verification page

        else:
            return render(request, 'otp_request.html', {'error_message': 'User not found'})

    return render(request, 'otp_request.html')


def otp_verify2(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        print(entered_otp)
        email = request.session.get('registration_email2')  # Get the email stored in the session

        if email:
            print(email)
            user = CustomUser.objects.filter(email=email).first()

            if user and entered_otp == user.otp:
                print("OTP verified")
                # OTP is valid, complete the registration process
                user.otp = None  # Clear the OTP field
                user.save()

                # Log in the user temporarily for OTP verification
                login(request, user)

                # Redirect to the login page
                if MedicalInformation.objects.filter(user=user).exists():
                    return redirect('medsuccess')  # Redirect to 'success' if medical information is already filled
                else:
                    return redirect('medinfo')  # Redirect to 'medinfo' if medical information is not filled
            else:
                print("OTP not verified")
                messages.error(request, 'Invalid OTP. Please try again.')
        else:
            print("Email not found in session")
            messages.error(request, 'Email not found in session. Please register again.')

    return render(request, 'otp_verify2.html')
