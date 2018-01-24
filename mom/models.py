from django.db import models

# Create your models here.

class Userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64,null=False,default="leo")
    email = models.CharField(max_length=64,null=False)
    password = models.CharField(max_length=64,null=False)

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    host = models.GenericIPAddressField(max_length=32,null=False)
    department = models.CharField(max_length=64,null=False)
    position = models.CharField(max_length=64,null=False)
    group = models.ForeignKey(to="Group",to_field="id",default=0)

    def __str__(self):
        return self.host


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    groupname = models.CharField(max_length=64,null=False)
    content = models.CharField(max_length=128)
    manager = models.CharField(max_length=64)

    def __str__(self):
        return self.groupname
