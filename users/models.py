from django.db import models
from django.contrib.auth.models import User



class ConfirmCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    valid_until = models.DateTimeField()