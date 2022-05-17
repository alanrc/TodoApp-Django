from django.contrib import admin
from task.models import Task
# from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','complete', 'created')

admin.site.register(Task, TaskAdmin)
