from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

import datetime

from libs.validators import phone_validator, validate_image_extension
from libs.fields import SizeRestrictedImageField
from libs.image_utils import update_file_path
from business_card_backend import settings
from .paths import PROFILE_PIC


def profile_pic_path(instance, filename):
    path = PROFILE_PIC + str(instance.id) + \
           datetime.datetime.now().strftime("/%Y-%m-%d/")
    return update_file_path(instance, filename, path, 'profile_pic')


class User(AbstractUser):
    email = models.EmailField(_('Email address'), blank=True, unique=True)
    phone_number = models.CharField(_("Contact Phone"), max_length=20,
                                     validators=[phone_validator],
                                     unique=True, blank=True,
                                     null=True)
    location =  models.CharField(_("Location"), max_length=100,
                                       blank=True, null=True)
    date_of_birth = models.DateField(_("Date of Birth"), blank=True, null=True)
    profile_pic = SizeRestrictedImageField(max_upload_size=5242880, verbose_name="Image",
                                     validators=[validate_image_extension], blank=True, null=True,
                                     upload_to=profile_pic_path)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Job(models.Model):
    title = models.CharField("Contact Address", max_length=100,
                                       blank=True, null=True)
    employee = models.ForeignKey(User, related_name="employee_jobs", on_delete=models.CASCADE)
    employer = models.ForeignKey(User, related_name="employer_jobs", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

