from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class ChatRoom(models.Model):
    """Foydalanuvchi va admin o'rtasidagi chat xonasi"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_chatrooms')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_chatrooms', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Chat xonasi'
        verbose_name_plural = 'Chat xonalari'

    def __str__(self):
        return f"{self.user.username} va admin o'rtasidagi chat"


class Message(models.Model):
    """Chatdagi xabarlar"""
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Xabar matni')
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField('Oʻqilgan', default=False)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'

    def __str__(self):
        return f"{self.sender.username} dan {self.timestamp.strftime('%Y-%m-%d %H:%M')} da xabar"