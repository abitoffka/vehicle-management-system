from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    firstname = models.CharField(max_length=100, default='Fistname')
    lastname = models.CharField(max_length=100, default='Lastname')
    email = models.EmailField(max_length=100, default='blank')

    def __str__(self) -> str:
        return self.user.username


