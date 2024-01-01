from django.db import models

# Create your models here.


class NormalCoup (models.Model):
    card_name = models.CharField(max_length=30)
    persian_name = models.CharField(max_length=30)
    active_ability = models.CharField(max_length=50, blank=True)
    passive_ability = models.CharField(max_length=50, blank=True)
    normal_check = models.IntegerField(max_length=1)
