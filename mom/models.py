from django.db import models

# Create your models here.

class Userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64,null=False,default="leo")
    email = models.CharField(max_length=64,null=False)
    password = models.CharField(max_length=64,null=False)

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    host = models.CharField(max_length=64,null=False)
    hostname = models.CharField(max_length=32,null=False)
    department = models.CharField(max_length=64,null=False)
    position = models.CharField(max_length=64,null=False)
    manager = models.CharField(max_length=64,null=False)

