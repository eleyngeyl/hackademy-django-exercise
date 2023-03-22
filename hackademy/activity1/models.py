from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture', null=True)
    description = models.TextField(max_length=250)