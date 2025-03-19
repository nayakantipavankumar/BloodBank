from django.db import models

# Create your models here.
class UserRegister(models.Model):
    Id=models.AutoField()
    Name= models.CharField(max_length=100)
    BloodGroup=models.CharField(max_length=3)
    City=models.CharField(max_length=30)
    State=models.CharField(max_length=50)
    Age=models.IntegerField()
