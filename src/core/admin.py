from django.contrib import admin

admin.site.site_header = "Notifications Admin"
admin.site.index_title = "Notifications"
admin.site.site_title = "Notifications Admin"


class BaseUserTrackingAdmin(admin.ModelAdmin):
    ordering = ("-created",)

    readonly_fields = ("uuid", "created_by", "updated_by")

    def created_(self, obj):
        return obj.created.strftime("%Y-%m-%d %H:%M:%S")

    created_.short_description = "Created"

    def updated_(self, obj):
        return obj.updated.strftime("%Y-%m-%d %H:%M:%S")

    updated_.short_description = "Updated"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
