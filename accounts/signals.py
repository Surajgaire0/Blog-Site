from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete
from django.contrib.auth import get_user_model
from .models import Profile
import cloudinary.uploader

@receiver(post_save,sender=get_user_model())
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=get_user_model())
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

#delete photo when user profile is deleted
@receiver(pre_delete, sender=Profile)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)