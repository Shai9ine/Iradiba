from django.urls import path
from .views import register, login_page, logout_page

urlpatterns = [
    path('register', register),
    path('login', login_page),
    path('logout', logout_page),
]
