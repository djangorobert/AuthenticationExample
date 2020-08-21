from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.


class CustomUser(AbstractUser):
    #telephone_number = models.CharField(max_length=20)
    pass