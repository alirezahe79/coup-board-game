from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.core.exceptions import ValidationError

user = get_user_model()


# Create your models here.


class NormalLobby(models.Model):
    players = models.ManyToManyField(to=user,
                                     validators=[MinValueValidator(2), MaxValueValidator(10)])
    is_plus = models.BooleanField(default=False)
    is_end = models.BooleanField(default=False)
    life_time = models.DateTimeField(auto_now_add=True)     # trigger on create
    scoreboard = models.TextField(blank=True)

    """def clean(self):
        min_player_count = 2
        if self.is_plus:
            min_player_count = 6
        if self.players.all().count()<min_player_count:
            raise ValidationError('moshkel dar tedad')"""
