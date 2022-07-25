from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.EmailField()
    Mobile_no=models.IntegerField()
    Password=models.CharField(max_length=10)

class Customer(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    city=models.CharField(max_length=10)