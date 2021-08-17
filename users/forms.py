from users.models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets

class DateInput(forms.DateInput):
    input_type = 'date'

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username']
        widgets = {'date_purchased': DateInput()}

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
