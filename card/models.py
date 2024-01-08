from django.db import models

# Create your models here.


class NormalCoup (models.Model):
    card_nam = models.CharField(max_length=30)
    persian_name = models.CharField(max_length=30)
    active_ability = models.TextField(blank=True)
    passive_ability = models.TextField(blank=True)
    is_normal = models.BooleanField(default=True)

    def __str__(self):
        return self.card_nam
