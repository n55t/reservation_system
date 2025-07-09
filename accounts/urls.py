from django.urls import path
from .views import CustomLoginView, SignUpView, SignUpSuccessView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/success/', SignUpSuccessView.as_view(), name='signup_success'),
]
