# Generated by Django 4.2.7 on 2024-01-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normalcoup',
            name='normal_check',
        ),
        migrations.AddField(
            model_name='normalcoup',
            name='is_normal',
            field=models.BooleanField(default=True),
        ),
    ]
