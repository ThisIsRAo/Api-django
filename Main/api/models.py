from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
def upload_thumbnail(instance,filename):
    path=f'thumbnails/{instance.username}'
    exitension=filename.split('.')[-1]
    if exitension:
        path=path+'.'+exitension
    return path



class User(AbstractUser):
    thumbnail=models.ImageField(
        upload_to=upload_thumbnail,
        null=True,
        blank=True
    )

class Student(models.Model):
    stuname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
