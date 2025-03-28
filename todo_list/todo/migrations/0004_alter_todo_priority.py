# Generated by Django 5.1.7 on 2025-03-27 07:17

import todo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('high', todo.models.TodoPriority['HIGH']), ('medium', todo.models.TodoPriority['MEDIUM']), ('low', todo.models.TodoPriority['LOW'])], default='medium', max_length=6),
        ),
    ]
