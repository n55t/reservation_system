from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm, EmailOrPhoneLoginForm


class CustomLoginView(LoginView):
    form_class = EmailOrPhoneLoginForm
    template_name = 'accounts/login.html'


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        messages.success(self.request, "アカウントを作成しました。")
        return super().form_valid(form)


class SignUpSuccessView(TemplateView):
    template_name = 'accounts/signup_success.html'
