from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseUUID(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True


class BaseCreatedUpdated(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseCreatedByUpdatedBy(models.Model):
    created_by = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_created_by",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        editable=False,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_updated_by",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        editable=False,
    )

    class Meta:
        abstract = True
