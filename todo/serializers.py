from django.db.models import fields
from rest_framework import serializers
from .models import Todo, TodoCategory
 
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'task',
            'description',
            'category',
            'due_date',
            'status',
            'order'
        )

class TodoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoCategory
        fields = (
            'id',
            'tag',
            'name',
        )
