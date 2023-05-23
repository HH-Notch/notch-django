from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class ToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toggle
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


class MorningMusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorningMusicList
        fields = '__all__'


class MorningDestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorningDestList
        fields = '__all__'