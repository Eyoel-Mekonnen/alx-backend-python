from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# 1. Custom User Model
class User(AbstractUser):
    # Add any extra fields here if needed (e.g., phone, profile_pic)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


# 2. Conversation Model
class Conversation(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id} between {[user.username for user in self.participants.all()]}"


# 3. Message Model
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:30]}"

