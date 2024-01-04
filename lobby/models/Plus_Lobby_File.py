from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class PlusLobby(models.Model):
    players = models.ManyToManyField(to=User,
                                     validators=[MinValueValidator(6), MaxValueValidator(10)])
    end_lobby = models.BooleanField(default=False)
    life_time = models.DateTimeField(auto_now_add=True)     # trigger on create
