from django.db import models
from django.utils import timezone

from users.models import User


class MessageManager(models.Manager):
    def read(self, user):
        return super().get_queryset().filter(read_at__isnull=False, to_user=user)

    def unread(self, user):
        return super().get_queryset().filter(read_at__isnull=True, to_user=user)


class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")

    title = models.CharField(max_length=50)
    body = models.TextField()

    read_at = models.DateTimeField(null=True, blank=True)

    objects = MessageManager()

    def mark_read(self):
        self.read_at = timezone.now()
        self.save()
