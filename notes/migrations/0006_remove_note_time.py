# Generated by Django 5.0.6 on 2024-06-17 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_note_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='time',
        ),
    ]
