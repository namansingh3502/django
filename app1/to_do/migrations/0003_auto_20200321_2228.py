# Generated by Django 3.0.4 on 2020-03-21 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='due date'),
        ),
    ]
