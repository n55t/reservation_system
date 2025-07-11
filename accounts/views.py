from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm, LoginForm


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        # フォームからemailとphoneを取得
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        password = form.cleaned_data.get('password')

        # authenticate関数にemailとphoneを渡す
        user = authenticate(self.request, email=email, phone=phone, password=password)

        if user is not None:
            # 認証成功
            return super().form_valid(form)
        else:
            # 認証失敗
            form.add_error(None, "メールアドレス/電話番号またはパスワードが正しくありません。")
            return self.form_invalid(form)



class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        messages.success(self.request, "アカウントを作成しました。")
        return super().form_valid(form)


class SignUpSuccessView(TemplateView):
    template_name = 'accounts/signup_success.html'
