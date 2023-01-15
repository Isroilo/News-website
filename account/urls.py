from django.urls import path
from .views import *

urlpatterns = [
    path('log-in/', signin_view, name='login_url'),
    path('log-up/', signup_view, name='register_url'),
    path('log-out/', logout_view, name='logout_url'),
]