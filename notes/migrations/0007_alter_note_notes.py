# Generated by Django 5.0.6 on 2024-06-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_remove_note_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='notes',
            field=models.CharField(default='', max_length=2048),
        ),
    ]
