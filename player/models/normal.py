from django.db import models
from django.contrib.auth import get_user_model
from card.models import NormalCoup
User = get_user_model()
# Create your models here.


class NormalPlayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    player_number = models.IntegerField()
    card1 = models.CharField(max_length=50, blank=True)
    card2 = models.CharField(max_length=50, blank=True)
    pocket = models.IntegerField()
    lose = models.IntegerField()
    normal_check = models.IntegerField()
