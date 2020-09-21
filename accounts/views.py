from django.views import generic,View
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import NewUserCreationForm, ProfileUpdateForm, UserUpdateForm
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from .models import Profile
from django.contrib.auth import get_user_model
from post.models import Posts

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

class NewLoginView(LoginView):
    template_name='accounts/login.html'

### Profile view 
class ProfileDetail(generic.TemplateView):
    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args,**kwargs)

    template_name='accounts/profile-detail.html'
    # def get(self,request,*args,**kwargs):
    #     # user=get_user_model().objects.get(profile__slug=self.kwargs['slug'])
    #     # #profile=get_object_or_404(Profile,slug=self.kwargs['slug'])
    #     # profile=Profile.objects.get(slug=self.kwargs['slug'])
    #     #user=get_user_model().objects.get(profile__slug=self.kwargs['slug'])
    #     #profile=Profile.objects.get(slug=self.kwargs['slug'])
    #     #is_owner=self.request.user==user
    #     #context={'user':user,'profile':profile,'is_owner':is_owner}
    #     return render(request,'accounts/profile-detail.html')

    def get_context_data(self,*args,**kwargs):
        ctx=super().get_context_data(*args,**kwargs)
        ctx['posts']=Posts.objects.filter(author=self.request.user)
        return ctx

class ProfileUpdateView(View):
    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args,**kwargs)

    def get(self,request,*args,**kwargs):
        profile_form=ProfileUpdateForm(instance=request.user.profile)
        user_form=UserUpdateForm(instance=request.user)
        return render(request,'accounts/profile-update.html',context={'profile_form':profile_form,'user_form':user_form})

    def post(self,request,*args,**kwargs):
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        user_form=UserUpdateForm(request.POST,instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile Updated')
            return HttpResponseRedirect(request.user.profile.get_absolute_url())
        return render(request,'accounts/profile-update.html',context={'profile_form':profile_form,'user_form':user_form})