from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class GoodMorningSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodMorning
        fields = ['user_name', 'weather_turn', 'todo_turn', 'music_turn']


class MorningMusicNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorningMusicList
        fields = ['name']


class MorningMusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorningMusicList
        fields = '__all__'


class MorningDestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorningDestList
        fields = ['name']


class MorningDestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorningDestList
        fields = ['id', 'name', 'address', 'url']


class GoodAfternoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodAfternoon
        fields = ['todo_turn', 'study_turn', 'nap_turn', 'nap_link']


class AfternoonStudyMusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfternoonStudyMusicList
        fields = '__all__'


class GoodEveningSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodEvening
        fields = ['user_name', 'today_feedback_turn', 'tomorrow_brief_turn', 'health_turn']


class EveningDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EveningDiary
        fields = ['diary_turn', 'brainer_turn']


class EveningSleepMusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveningSleepMusicList
        fields = '__all__'
