from .models import ToDoElements
from rest_framework import serializers


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoElements
        fields = ['id', 'todo_text', 'done']
