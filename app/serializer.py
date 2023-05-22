from rest_framework import serializers
from .models import *
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class ToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toggle
        fields = '__all__'
