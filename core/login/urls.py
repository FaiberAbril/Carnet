from django.urls import path
from core.login.views import *


urlpatterns = [
    path('',loginFormView.as_view(), name='login'),
    path('logout/',logoutFormView.as_view(), name='logout'),
]