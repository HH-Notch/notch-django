from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import AccountManager


class Account(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, null=False, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    # spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email

class Toggle(models.Model):
    mor_todo = models.BooleanField(default=False)
    mor_depart = models.BooleanField(default=False)
    mor_dest = models.BooleanField(default=False)
    mor_weather = models.BooleanField(default=False)
    aft_todo =  models.BooleanField(default=False)
    aft_whitenoise =  models.BooleanField(default=False)
    aft_nap =  models.BooleanField(default=False)
    eve_progress =  models.BooleanField(default=False)
    eve_health =  models.BooleanField(default=False)
    eve_question =  models.BooleanField(default=False)
    eve_todo =  models.BooleanField(default=False)
    eve_play =  models.BooleanField(default=False)