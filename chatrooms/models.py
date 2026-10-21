from django.db import models

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    chatroom = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)