from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.TaskStructure)
class TaskStructureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

    fieldsets = (

        ("information", {"fields": ('task_structure_id', 'title', 'description', 'cycle_time')}),

    )

    list_filter = ["title", ]


@admin.register(models.SubTaskStructure)
class SubTaskStructureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

    fieldsets = (

        ("information", {"fields": ('title', 'description', 'sub_task_structure_id',
                                    'task_structure')}),

    )

    list_filter = ["title", ]


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['start_task_time', 'deadline', ]

    fieldsets = (

        ("information", {"fields": ('task_id', 'start_task_time', 'deadline', 'task_structure')}),

    )

    list_filter = ["start_task_time", ]


@admin.register(models.SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['sub_task_id', 'task_status', ]

    fieldsets = (

        ("information", {"fields": ('task_status', 'sub_task_id', 'trouble_description', 'task',
                                    'sub_task_structure',)}),

    )

    list_filter = ["sub_task_id", ]


@admin.register(models.TaskUser)
class TaskUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'last_name', 'phone_number',]

    fieldsets = (

        ("information", {"fields": ('username', 'name', 'last_name', 'phone_number',
                                    'user', 'task_structure')}),

    )

    list_filter = ["username", ]
