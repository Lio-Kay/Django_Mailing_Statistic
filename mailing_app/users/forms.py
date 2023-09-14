from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = 'email', 'password1', 'password2'


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = 'email', 'avatar'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
