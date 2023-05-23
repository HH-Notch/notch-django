from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(Toggle)
admin.site.register(MorningBlock)
admin.site.register(AfternoonBlock)
admin.site.register(EveningBlock)
admin.site.register(MorningMusicList)
admin.site.register(MorningDestList)
