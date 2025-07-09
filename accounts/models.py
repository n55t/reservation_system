from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid # uuidをインポート


class CustomUser(AbstractUser):
    # usernameのユニーク制約を外し、必須ではなくし、デフォルト値を設定
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,  # ユニーク制約を解除
        blank=True, # 必須ではない
        null=True, # DBでもNULLを許容
        default=uuid.uuid4, # デフォルト値をUUIDに設定
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    # emailをユニークにし、必須項目とする
    email = models.EmailField(_("email address"), unique=True)

    # 氏名（かな）
    last_name_kana = models.CharField("姓（かな）", max_length=150, blank=True)
    first_name_kana = models.CharField("名（かな）", max_length=150, blank=True)

    # 電話番号
    phone = models.CharField("電話番号", max_length=20, unique=True, null=True, blank=True)

    # 生年月日
    birth_date = models.DateField("生年月日", null=True, blank=True)

    # 住所
    postal_code = models.CharField("郵便番号", max_length=7, blank=True)
    prefecture = models.CharField("都道府県", max_length=40, blank=True)
    city = models.CharField("市区町村", max_length=100, blank=True)
    street_address = models.CharField("番地など", max_length=255, blank=True)
    building_name = models.CharField("建物名・部屋番号", max_length=255, blank=True)

    # ログインIDをemailに変更
    USERNAME_FIELD = 'email'
    # ユーザー作成時に必須とするフィールド（USERNAME_FIELDは含めない）
    REQUIRED_FIELDS = [] # usernameを必須から外す

    def __str__(self):
        return self.username

