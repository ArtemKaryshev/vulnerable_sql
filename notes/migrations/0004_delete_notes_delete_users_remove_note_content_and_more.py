# Generated by Django 5.0.6 on 2024-06-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notes',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RemoveField(
            model_name='note',
            name='content',
        ),
        migrations.AddField(
            model_name='note',
            name='notes',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]
