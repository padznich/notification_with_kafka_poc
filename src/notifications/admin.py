from django.contrib import admin

from core.admin import BaseUserTrackingAdmin
from notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(BaseUserTrackingAdmin):
    list_display = ("uuid", "status", "name", "subject", "sender", "created_", "updated_", "created_by", "updated_by")
    list_filter = ("status",)
    search_fields = ("name", "subject")
