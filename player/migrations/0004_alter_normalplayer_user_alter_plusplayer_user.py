# Generated by Django 4.2.7 on 2024-01-05 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0003_rename_end_lobby_normallobby_is_end_and_more'),
        ('player', '0003_remove_normalplayer_lose_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normalplayer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobby.normallobby'),
        ),
        migrations.AlterField(
            model_name='plusplayer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobby.pluslobby'),
        ),
    ]
