from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField
from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

class NewUserCreationForm(UserCreationForm):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    email=forms.EmailField()
    recaptcha=ReCaptchaField()

    class Meta:
        model=get_user_model()
        fields=['first_name','last_name','username','email','password1','password2','recaptcha']

class UserUpdateForm(forms.ModelForm):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)

    class Meta:
        model=get_user_model()
        fields=('first_name','last_name','username','email')

class ProfileUpdateForm(forms.ModelForm):
    website=forms.URLField(required=False)
    profile_picture=forms.ImageField()

    class Meta:
        model=Profile
        fields=('profile_picture','website')