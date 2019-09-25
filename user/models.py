from django.db import models


# Create your models here.
class User1(models.Model):
    account_number= models.IntegerField(default=0)
    phone_number=models.IntegerFiled(max_length=10,default=0000000000)
    name=models.CharField(default=0)
