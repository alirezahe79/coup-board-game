from django.db import models
from lobby.models import NormalLobby
import json
# Create your models here.


class NormalGame (models.Model):
    players = models.ForeignKey(NormalLobby, on_delete=models.CASCADE)
    is_start = models.BooleanField(default=True)
    card_storage = models.TextField(blank=True, null=True, default='{}')        # need to send dict as string in db
    players_gold_storage = models.TextField(blank=True, null=True, default='{}')

    def save(self, *args, **kwargs):
        # load the current string and
        # convert string to python dictionary
        # if it is empty, save it back to a '{}' string,
        # if it is not empty, convert the dictionary back to a json string
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
        super(NormalGame, self).save(*args, **kwargs)
