# Generated by Django 4.2.7 on 2024-01-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NormalCoup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=30)),
                ('persian_name', models.CharField(max_length=30)),
                ('active_ability', models.TextField(blank=True)),
                ('passive_ability', models.TextField(blank=True)),
                ('normal_check', models.IntegerField()),
            ],
        ),
    ]
