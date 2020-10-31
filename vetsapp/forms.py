from .models import application
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import LoginForm, SignupForm

ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'allauth.account.forms.SignupForm',
}


class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)


class MyCustomSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent classes save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

class RegisterForm(UserCreationForm):
    """
    docstring
    """
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]


# def UserLoginForm(AuthenticationForm):
#     """
#     login view
#     """
#     username = forms.CharField(
#         label='Логин',
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#         )
#     password = forms.CharField(
#         label='Пароль',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#         )


class applicationForm(ModelForm):
    """
    docstring
    """
    class Meta:
        model = application
        fields = '__all__'
