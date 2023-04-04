from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseCreatedByUpdatedBy, BaseCreatedUpdated, BaseUUID

User = get_user_model()


class NotificationStatus(models.IntegerChoices):
    CREATED = 0
    SCHEDULED = 1
    RUNNING = 2
    SENT = 3
    SUCCEED = 4
    FAILED = 5


class Notification(BaseUUID, BaseCreatedUpdated, BaseCreatedByUpdatedBy):
    name = models.CharField(max_length=1024, blank=True, null=True)
    subject = models.CharField(max_length=1024, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=NotificationStatus.choices, blank=True, default=NotificationStatus.CREATED)
    user_set = models.ManyToManyField(User, related_name="notification_set_receiver")
    sender = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="notification_set_sender"
    )

    class Meta:
        ordering = ["-updated"]
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")

    def __str__(self):
        return self.name or ""
