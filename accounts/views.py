from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import NewUserCreationForm

# Create your views here.
class SignUpView(SuccessMessageMixin,generic.CreateView):
    form_class=NewUserCreationForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'

    def get_success_message(self,*args,**kwargs):
        return 'You signed up. Login to continue.'

class NewPasswordResetView(PasswordResetView):
    template_name='accounts/password_reset_form.html'
    
class NewPasswordResetCompleteView(PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'