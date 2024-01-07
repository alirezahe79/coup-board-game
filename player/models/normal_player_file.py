from django.db import models
from lobby.models import NormalLobby
# Create your models here.


class NormalPlayer(models.Model):
    user = models.ForeignKey(NormalLobby, on_delete=models.CASCADE)
    player_number = models.IntegerField()
    card1 = models.CharField(max_length=50, blank=True)
    card2 = models.CharField(max_length=50, blank=True)
    pocket = models.IntegerField()
    is_lose = models.BooleanField(default=False)
    is_normal = models.BooleanField(default=True)
