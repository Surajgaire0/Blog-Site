from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField

class NewUserCreationForm(UserCreationForm):
    recaptcha=ReCaptchaField()

    #class Meta:
    #    fields=['username','email','password','recaptcha']
