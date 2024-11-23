from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'timestamp', 'chatroom']

    def validate(self, data):
        chatroom = data['chatroom']
        sender = self.context['request'].user

        if sender not in chatroom.participants.all():
            raise serializers.ValidationError("User is not a participant in this chatroom.")
        
        return data