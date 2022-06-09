from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import LoginCode


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class ConfirmForm(forms.ModelForm):
    code = forms.CharField(label='Введите код подтверждения')
    user = forms.CharField(label='Подтвердите имя пользователя')

    class Meta:
        model = LoginCode
        fields = ['user', 'code']
