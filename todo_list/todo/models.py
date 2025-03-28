from django.db import models

from enum import Enum


class TodoPriority(Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

    def __str__(self):
        return str(self.value)


PRIORITY_TUPLE = {
    'high': TodoPriority.HIGH,
    'medium': TodoPriority.MEDIUM,
    'low': TodoPriority.LOW
}


class Todo(models.Model):
    """Main model for todo app."""
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True)
    completed_date = models.DateField(null=True, blank=True)
    priority = models.CharField(
        max_length=6, choices=PRIORITY_TUPLE, default='medium'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_completed(self):
        return self.completed_date is not None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date', 'created_at']
