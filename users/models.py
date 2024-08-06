from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PersonalToken(models.Model):
    token = models.CharField(max_length=255,null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models,models.DateTimeField(auto_now=True)





