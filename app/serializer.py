from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name']  # 'spouse_name', 'date_of_birth'


class ToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toggle
        fields = '__all__'
