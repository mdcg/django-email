from django.contrib.auth.models import User
from django.db import models


class ConfirmationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation_key = models.CharField(max_length=100)
    is_confirmed = models.BooleanField(default=False)
