from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class ScoreBoard(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    win = models.IntegerField(default=0, blank=True)
    lose = models.IntegerField(default=0, blank=True)
    win_rate = models.IntegerField(default=0, blank=True)
    total_score = models.IntegerField(default=0, blank=True)
