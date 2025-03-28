from rest_framework import serializers

from todo.models import PRIORITY_TUPLE
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def create(self, validated_data: dict) -> Todo:
        """
        Create and return a new 'Todo' item.
        """
        return Todo.objects.create(**validated_data)

    def update(self, instance: Todo, validated_data: dict) -> Todo:
        """
        Update and save a 'Todo' item.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.due_date = validated_data.get(
            'due_date', instance.due_date
        )
        instance.completed_date = validated_data.get(
            'completed_date', instance.completed_date
        )
        instance.priority = validated_data.get(
            'priority', instance.priority
        )
        instance.save()
        return instance
