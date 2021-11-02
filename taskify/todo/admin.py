from django.contrib import admin

from .models import TaskList, Task


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_datetime', 'updated_datetime', 'title')
    list_filter = ('created_datetime', 'updated_datetime')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_datetime',
        'updated_datetime',
        'title',
        'status',
    )
    list_filter = ('created_datetime', 'updated_datetime', 'status')
