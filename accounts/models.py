from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # 氏名（かな）
    last_name_kana = models.CharField("姓（かな）", max_length=150, blank=True)
    first_name_kana = models.CharField("名（かな）", max_length=150, blank=True)

    # 電話番号
    phone = models.CharField("電話番号", max_length=20, blank=True)

    # 生年月日
    birth_date = models.DateField("生年月日", null=True, blank=True)

    # 住所
    postal_code = models.CharField("郵便番号", max_length=7, blank=True)
    prefecture = models.CharField("都道府県", max_length=40, blank=True)
    city = models.CharField("市区町村", max_length=100, blank=True)
    street_address = models.CharField("番地など", max_length=255, blank=True)
    building_name = models.CharField("建物名・部屋番号", max_length=255, blank=True)

    def __str__(self):
        return self.username
