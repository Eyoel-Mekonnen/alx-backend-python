# messaging_app/chats/serializers.py

from rest_framework import serializers
from .models import User, Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):
    # Include nested messages inside a conversation
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages']  # Adjust fields as per your model


class UserSerializer(serializers.ModelSerializer):
    # Example of SerializerMethodField
    full_name = serializers.SerializerMethodField()
    phone_number = serializers.CharField(max_length=15)
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'full_name']  # Adjust fields as per your model

    def get_full_name(self, obj):
        # Assuming your User model has first_name and last_name fields
        return f"{obj.first_name} {obj.last_name}"

    def validate_phone_number(self, value):
        # Example validator raising ValidationError if invalid phone number
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain digits only.")
        return value

