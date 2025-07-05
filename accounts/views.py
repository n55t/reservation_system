from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'ユーザー名'})
        form.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'パスワード'})
        return form
