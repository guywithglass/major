from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contract(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    crop = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    message = models.TextField()
    accepted = models.BooleanField(default=False)
    accepted_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username
