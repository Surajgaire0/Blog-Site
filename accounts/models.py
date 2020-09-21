from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name='profile')
    slug=models.SlugField(unique=True)
    website=models.URLField(blank=True)
    #profile_picture=models.ImageField(upload_to='profile',default='default1.png',blank=True,null=True)
    profile_picture=CloudinaryField('profile_picture',default='v1600368583/default1_pictures.png.png')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile-detail')

    def save(self,*args,**kwargs):
        self.slug=slugify(self.user.username)
        return super().save(*args,**kwargs)