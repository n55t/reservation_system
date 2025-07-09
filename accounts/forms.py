from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
import re
from datetime import date


class LoginForm(AuthenticationForm):
    """ログインフォームを電話番号またはメールアドレス用に変更"""
    email = forms.EmailField(
        label="メールアドレス",
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'メールアドレスを入力してください'})
    )
    phone = forms.CharField(
        label="電話番号",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '電話番号を入力してください'})
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        if not email and not phone:
            raise forms.ValidationError(
                "メールアドレスまたは電話番号のいずれかを入力してください。",
                code='no_identifier'
            )
        elif email and phone:
            raise forms.ValidationError(
                "メールアドレスと電話番号は同時に指定できません。",
                code='both_identifiers'
            )

        # 認証バックエンドに渡すための 'username' フィールドを設定
        if email:
            self.cleaned_data['username'] = email
        elif phone:
            self.cleaned_data['username'] = phone

        return self.cleaned_data


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username', 'email', # emailを先頭の方へ
            'last_name', 'first_name', 'last_name_kana', 'first_name_kana',
            'birth_date', 'phone',
            'postal_code', 'prefecture', 'city', 'street_address', 'building_name'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # フィールドのラベルを日本語に設定
        self.fields['last_name'].label = "姓"
        self.fields['first_name'].label = "名"
        self.fields['last_name_kana'].label = "姓（かな）"
        self.fields['first_name_kana'].label = "名（かな）"
        self.fields['username'].label = "ユーザー名"
        self.fields['email'].label = "メールアドレス"
        self.fields['birth_date'].label = "生年月日"
        self.fields['phone'].label = "電話番号"
        self.fields['postal_code'].label = "郵便番号"
        self.fields['prefecture'].label = "都道府県"
        self.fields['city'].label = "市区町村"
        self.fields['street_address'].label = "番地など"
        self.fields['building_name'].label = "建物名・部屋番号"

        # 生年月日のウィジェットをSelectDateWidgetに変更
        years = range(date.today().year - 100, date.today().year + 1)
        self.fields['birth_date'].widget = forms.SelectDateWidget(years=years)

        # プレースホルダーとCSSクラスの設定
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name not in ['birth_date']:
                field.widget.attrs['placeholder'] = field.label

        # 電話番号のヘルプテキスト
        self.fields['phone'].help_text = "ハイフンなしで入力してください。"

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # 数字以外の文字をすべて削除
            return re.sub(r'\D', '', phone)
        return phone

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if not email and not phone:
            raise forms.ValidationError(
                "メールアドレスまたは電話番号のいずれかを入力してください。",
                code='no_identifier'
            )
        return cleaned_data
