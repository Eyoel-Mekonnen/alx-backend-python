from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email']  # adjust fields as per your User model


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)  # nested sender details (assuming FK)
    
    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'content', 'timestamp']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)  # many to many users
    messages = MessageSerializer(many=True, read_only=True)  # nested messages

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages', 'created_at']

