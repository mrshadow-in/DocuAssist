"""medgpt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register/regcomplete/', views.regcomplete, name='regcomplete'),
    path('success/', views.success, name='success'),
    path('medinfo/', views.medinfo, name='medinfo'),  # Add URL pattern for medinfo
    # Add a URL pattern to handle the submission of medical information
    path('medcomplete/', views.medcomplete, name='medcomplete'),
    path('medsuccess/', views.medsuccess, name='medsuccess'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('upload_diagnostic_report/', views.upload_diagnostic_report, name='upload_diagnostic_report'),
    path('upload_success/', views.upload_success, name='upload_success'),
    path('myuploads/', views.myuploads, name='myuploads'),

]
