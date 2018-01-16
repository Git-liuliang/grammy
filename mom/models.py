from django.db import models

# Create your models here.

class Userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=64,null=False)
    password = models.CharField(max_length=64,null=False)

