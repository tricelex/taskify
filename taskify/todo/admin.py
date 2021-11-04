from django.contrib import admin

from .models import Task, TaskList


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "created_datetime",
        "updated_datetime",
    )
    list_filter = ("created_datetime", "updated_datetime")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_datetime",
        "updated_datetime",
        "title",
        "status",
    )
    list_filter = ("created_datetime", "updated_datetime", "status")
