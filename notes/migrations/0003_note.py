# Generated by Django 5.0.6 on 2024-06-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_delete_person_users_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
