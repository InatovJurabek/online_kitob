from rest_framework import serializers
from apps.book.models import CustomUser


class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'address']
        