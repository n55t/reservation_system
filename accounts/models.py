from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    address = models.CharField("住所", max_length=255, blank=True)
    birth_date = models.DateField("生年月日", null=True, blank=True)
    phone = models.CharField("電話番号", max_length=20, blank=True)
    postal_code = models.CharField("郵便番号", max_length=10, blank=True)

    def __str__(self):
        return self.username
