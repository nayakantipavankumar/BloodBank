from django.shortcuts import render
from .models import UserRegister

# Create your views here.

def UserRegisterView(request):
    Data=request.POST
    print(Data)
    return render("submitted.html")