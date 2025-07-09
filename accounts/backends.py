from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # emailか電話番号でユーザーを検索。入力が空の場合は除外する。
            user = UserModel.objects.get(Q(email=username) | Q(phone=username))
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
