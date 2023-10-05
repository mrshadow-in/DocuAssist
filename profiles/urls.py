from django.urls import path
from . import views

urlpatterns = [
    path('my/', views.my_profile, name='my_profile'),
    path('my_edit/', views.edit_my_profile, name='my_edit'),
    path('mediinfoview/', views.medical_information, name='mediinfoview'),
    path('medinfo_edit/', views.edit_medical_information, name='medinfo_edit'),
    path('myreports/', views.my_reports, name='myreports'),
    #path('delete_report/<int:report_id>/', views.delete_report, name='delete_report'),

]
