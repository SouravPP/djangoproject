from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)