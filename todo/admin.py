from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Todo)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'task',
        'description',
        'category',
        'due_date',
        'status',
        'order',
        )