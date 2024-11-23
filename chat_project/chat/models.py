from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, related_name='chatrooms')

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Enforce that the sender must be a participant of the chatroom
        if self.sender not in self.chatroom.participants.all():
            raise ValidationError("User is not a participant in this chatroom.")

    def save(self, *args, **kwargs):
        # Call the clean method before saving
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.sender.username}: {self.content[:20]}'
class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
