from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('register/',UserRegisterView)
]