from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView

# Create your views here.
class SignUpView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'

class NewPasswordResetView(PasswordResetView):
    template_name='accounts/password_reset_form.html'
    
class NewPasswordResetCompleteView(PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'