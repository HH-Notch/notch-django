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
    # email = models.ForeignKey('Account', on_delete=models.CASCADE)
    mor_todo = models.IntegerField(default=1)
    mor_depart = models.IntegerField(default=1)
    mor_dest = models.IntegerField(default=1)
    mor_weather = models.IntegerField(default=1)
    aft_todo = models.IntegerField(default=1)
    aft_whitenoise = models.IntegerField(default=1)
    aft_nap = models.IntegerField(default=1)
    eve_progress = models.IntegerField(default=1)
    eve_health = models.IntegerField(default=1)
    eve_question = models.IntegerField(default=1)
    eve_todo = models.IntegerField(default=1)
    eve_play = models.IntegerField(default=1)
