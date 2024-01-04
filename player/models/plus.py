from django.db import models
from Base.lobby.models import PlusLobby
# Create your models here.


class PlusPlayer(models.Model):
    user = models.ForeignKey(PlusLobby, on_delete=models.CASCADE)
    lobby_number = models.IntegerField()
    card1 = models.CharField(max_length=50, blank=True)
    card2 = models.CharField(max_length=50, blank=True)
    pocket = models.IntegerField()
    party = models.IntegerField()
    is_lose = models.BooleanField(default=False)
