import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model extending AbstractUser with additional fields
class User(AbstractUser):
    # Use UUID as primary key if you want:
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128)
    # Email is already in AbstractUser, but you can enforce uniqueness here if needed
    email = models.EmailField(unique=True)

    # Optional: override first_name, last_name if you want custom max_length or behavior

    def __str__(self):
        return self.username

# Conversation model tracking users involved
class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id}"

# Message model linked to sender and conversation
class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message {self.message_id} from {self.sender.username}"

