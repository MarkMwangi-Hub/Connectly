from django.contrib.auth.management.commands.changepassword import UserModel
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Choices


class Member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    dateofbirth=models.DateField(blank=True,null=True)
    course = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name