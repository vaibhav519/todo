from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': "Your Email"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs["class"] = 'form-control form-control-lg'
        self.fields['username'].widget.attrs["placeholder"] = 'Your Name'
        self.fields['password1'].widget.attrs["class"] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs["placeholder"] = 'Password'
        self.fields['password2'].widget.attrs["class"] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs["placeholder"] = 'Repeat Password'
