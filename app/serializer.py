from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class GoodMorningSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodMorning
        fields = '__all__'


# class MorningMusicNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MorningMusicList
#         fields = '__all__'


class MorningMusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorningMusicList
        fields = '__all__'


# class MorningDestNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MorningDestList
#         fields = '__all__'


class MorningDestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorningDestList
        fields = ['id', 'name', 'address', 'link']


class GoodAfternoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodAfternoon
        fields = ['todo_turn', 'study_turn', 'nap_turn', 'sleep_turn', 'sleep_time']


# class AfternoonNapMusicNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AfternoonNapMusicList
#         fields = '__all__'


class AfternoonNapMusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfternoonNapMusicList
        fields = '__all__'


# class AfternoonStudyMusicNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AfternoonStudyMusicList
#         fields = '__all__'


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


# class EveningSleepMusicNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EveningSleepMusicList
#         fields = '__all__'


class EveningSleepMusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveningSleepMusicList
        fields = '__all__'


class MorningBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorningBlock
        fields = '__all__'


class AfternoonBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfternoonBlock
        fields = '__all__'


class EveningBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveningBlock
        fields = '__all__'
