from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

# Create your models here.


class SignUp(models.Model):
    fullname = models.CharField(max_length=250, blank=False)
    bday = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.fullname



