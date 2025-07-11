from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        email = kwargs.get('email')
        phone = kwargs.get('phone')

        user = None
        if email:
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                pass
        
        if not user and phone:
            try:
                user = UserModel.objects.get(phone=phone)
            except UserModel.DoesNotExist:
                pass

        if user and user.check_password(password):
            return user
        return None
