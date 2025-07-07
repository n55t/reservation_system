from django.contrib import admin
from django.urls import path, include

from accounts.views import CustomLoginView, SignUpView

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
