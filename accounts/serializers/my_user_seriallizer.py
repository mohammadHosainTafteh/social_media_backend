from rest_framework import serializers

from accounts.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'user', 'phone_number']
