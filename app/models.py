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


# 단축어에서 GET
class GoodMorning(models.Model):
    user_name = models.CharField(max_length=50, null=False, default='')
    weather_turn = models.IntegerField(null=False, default=1)
    todo_turn = models.IntegerField(null=False, default=1)
    music_turn = models.IntegerField(null=False, default=1)
    pathfind_turn = models.IntegerField(null=False, default=1)


# List 네 가지
class MorningMusicList(models.Model):
    name = models.CharField(max_length=50, null=False, default='')
    link = models.CharField(max_length=150, null=False, default='')


class MorningDestList(models.Model):
    name = models.CharField(max_length=50, null=False, default='')
    address = models.CharField(max_length=100, null=False, default='')
    latitude = models.CharField(max_length=20, null=False, default='')
    longtitude = models.CharField(max_length=20, null=False, default='')
    url = models.CharField(max_length=150, null=False, default='')


class GoodAfternoon(models.Model):
    todo_turn = models.IntegerField(null=False, default=1)
    study_turn = models.IntegerField(null=False, default=1)
    nap_turn = models.IntegerField(null=False, default=1)
    nap_link = models.CharField(max_length=150, null=False, default='')


class AfternoonStudyMusicList(models.Model):
    name = models.CharField(max_length=50, null=False, default='')
    link = models.CharField(max_length=150, null=False, default='')


class GoodEvening(models.Model):
    user_name = models.CharField(max_length=50, null=False, default='')
    today_feedback_turn = models.IntegerField(null=False, default=1)
    tomorrow_brief_turn = models.IntegerField(null=False, default=1)
    health_turn = models.IntegerField(null=False, default=1)


class EveningDiary(models.Model):
    diary_turn = models.IntegerField(null=False, default=1)
    brainer_turn = models.IntegerField(null=False, default=1)


class EveningSleepMusicList(models.Model):
    name = models.CharField(max_length=50, null=False, default='')
    link = models.CharField(max_length=150, null=False, default='')





