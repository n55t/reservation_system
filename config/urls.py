from django.contrib import admin
from django.urls import path, include

from accounts.views import CustomLoginView, SignUpView, SignUpSuccessView

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/success/', SignUpSuccessView.as_view(), name='signup_success'),
    path('schedule/', include('schedule.urls')),
]
