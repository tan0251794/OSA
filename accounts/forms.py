from accounts.models import UserAccounts
from django.contrib.auth.models import User
from django import forms 
from django.core.exceptions import ObjectDoesNotExist

class AccountForm(forms.Form):
    name = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="email", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirm", widget=forms.PasswordInput)

    def check_password(self):
        if "password" in self.cleaned_data:
            pass1 = self.cleaned_data['password']
            pass2 = self.cleaned_data['password2']
            if pass1 == pass2 and pass1:
                return pass1
        raise forms.ValidationError('password inputted is valid!')

    def check_username(self):
        name = self.cleaned_data['name']
        try:
            UserAccounts.objects.get(name = name)
        except ObjectDoesNotExist:
            return name
        raise forms.ValidationError('username has been existed!')

    def save(self):
        self.check_password()
        self.check_username()
        UserAccounts.objects.create_user(name=self.cleaned_data['name'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])