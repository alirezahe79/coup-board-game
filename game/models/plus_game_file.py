from django.db import models
from player.models import PlusPlayer
import json
# Create your models here.


class PlusGame (models.Model):
    players = models.ForeignKey(PlusPlayer, on_delete=models.CASCADE)
    is_start = models.BooleanField(default=True)
    card_storage = models.TextField(blank=True, null=True, default='{}')
    players_gold_storage = models.TextField(blank=True, null=True, default='{}')

    def save(self, *args, **kwargs):
        card_dict = json.loads(self.card_storage)
        if card_dict:
            self.card_storage = json.dumps(card_dict)
        else:
            self.card_storage = '{}'
        gold_dict = json.loads(self.players_gold_storage)
        if gold_dict:
            self.card_storage = json.dumps(gold_dict)
        else:
            self.players_gold_storage = '{}'
        super(PlusGame, self).save(*args, **kwargs)
