from django.shortcuts import render
from .models import UserRegister

# Create your views here.

def UserRegisterView(request):
    Data=request.POST
    print(Data)
    print("user name is : ", Data['your_name'])
    return render(request,"register.html",Data)