from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'username', 'autocomplete': 'username'}),
        label='نام کاربری:',
        error_messages={'required': 'نام کاربری اجباری می باشد. لطفا وارد کنید'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', 'autocomplete': 'current-password'}),
        label='رمز عبور:',
        error_messages={'required': 'رمز عبور اجباری میباشد لطفا آن را وارد کنید'}
    )
