from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# Create your models here.


class Student(models.Model):
    name=models.TextField()
    phone=models.TextField()
    number=models.TextField(unique=True)