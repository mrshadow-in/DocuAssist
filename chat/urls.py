from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_page, name='chat_page'),
    # Add more URL patterns for other chat-related views as needed
]
