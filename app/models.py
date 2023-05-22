from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import AccountManager


class Account(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, null=False, default='')
    password = models.CharField(max_length=20, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    # spouse_name = models.CharField(blank=True, max_length=100)
    # date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email


class Toggle(models.Model):
    # id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE)

    mor_weather = models.IntegerField(default=1)
    mor_todo = models.IntegerField(default=1)
    mor_dest = models.IntegerField(default=1)
    mor_pathfind = models.IntegerField(default=1)

    aft_todo = models.IntegerField(default=1)
    aft_whitenoise = models.IntegerField(default=1)
    aft_nap = models.IntegerField(default=1)

    eve_health = models.IntegerField(default=1)
    eve_progress = models.IntegerField(default=1)
    eve_question = models.IntegerField(default=1)
    eve_todo = models.IntegerField(default=1)
    eve_sleep = models.IntegerField(default=1)


class MorningWeather(models.Model):
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=False, default='weather')
    text = models.CharField(max_length=15, null=False, default='오늘의 날씨 알려주기')
    turn = models.IntegerField(null=False, default=1)


class MorningTodo(models.Model):
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=False, default='todo')
    text = models.CharField(max_length=15, null=False, default='오늘의 할일 브리핑')
    turn = models.IntegerField(null=False, default=1)


class MorningPathfind(models.Model):
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=False, default='destination')
    text = models.CharField(max_length=15, null=False, default='목적지까지 길찾기')
    turn = models.IntegerField(null=False, default=1)
    dest_list = models.TextField(null=True)


class MorningDestList(models.Model):
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, default='')
    link = models.CharField(max_length=150, null=False, default='')

