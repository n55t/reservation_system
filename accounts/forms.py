from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'address', 'birth_date', 'phone', 'postal_code')
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'address': '住所',
            'birth_date': '生年月日',
            'phone': '電話番号',
            'postal_code': '郵便番号',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
