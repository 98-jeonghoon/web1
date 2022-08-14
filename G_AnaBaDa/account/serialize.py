from dataclasses import field
from account.models import User
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            nickname=validated_data['nickname'],
            name=validated_data['name'],
            password=validated_data['password1'],
            password=validated_data['password2'],
            account_id=validated_data['account_id'],
            phone_number=validated_data['phone_number']
        )
        return user
    class Meta:
        model = User
        fields = '__all__'