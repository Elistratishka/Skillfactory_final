from django.urls import path, include
from .views import Register, SignIn, confirm


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', SignIn.as_view(), name='login'),
    path('confirm/', confirm, name='login_confirm'),
    path('', include('django.contrib.auth.urls')),
    ]

