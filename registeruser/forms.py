from django import forms
import re
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(label=u'Username', max_length=30)
    email = forms.EmailField(label=u'Email')
    password1 = forms.CharField(
        label=u'Password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=u'Password (Again)',
        widget=forms.PasswordInput()
    )
def clean_password2(self):
    if 'password1' in self.cleaned_data:
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
    raise forms.ValidationError('Passwords do not match.')

def clean_username(self):
    username = self.cleaned_data['username']
    if not re.search(r'^\w+$', username):
        raise forms.ValidationError('Username can only contain '
                    'alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

class LoginForm(AuthenticationForm):
    required_css_class = 'required'

    def clean_username(self):
        username = self.cleaned_data.get('username')
        self.cleaned_data['username'] = username.lower()
        return self.cleaned_data['username']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        self.check_for_username_and_password(password, username)
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_username_and_password(self, password, username):
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Please enter a correct email and password.")
