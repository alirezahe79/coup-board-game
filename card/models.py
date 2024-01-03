from django.db import models

# Create your models here.


class NormalCoup (models.Model):
    card_name = models.CharField(max_length=30)
    persian_name = models.CharField(max_length=30)
    active_ability = models.TextField(blank=True)
    passive_ability = models.TextField(blank=True)
    normal_check = models.IntegerField()
