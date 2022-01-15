from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aadhar_no = models.TextField(max_length=100)
    # file will be uploaded to MEDIA_ROOT / uploads
    image = models.ImageField(default='default.jpg', upload_to='uploads/')

    # or...
    # file will be saved to MEDIA_ROOT / uploads / 2015 / 01 / 30
    # upload = models.ImageField(upload_to='uploads/% Y/% m/% d/')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
