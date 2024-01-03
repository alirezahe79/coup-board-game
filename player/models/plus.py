from django.db import models
from django.contrib.auth import get_user_model
from card.models import NormalCoup
User = get_user_model()
# Create your models here.


class PlusPlayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lobby_number = models.IntegerField()
    card1 = models.CharField(max_length=50, blank=True)
    card2 = models.CharField(max_length=50, blank=True)
    pocket = models.IntegerField()
    party = models.IntegerField()
    is_lose = models.BooleanField(default=False)
