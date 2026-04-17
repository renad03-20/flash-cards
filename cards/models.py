from django.db import models
from decks.models import Deck

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front_q = models.TextField()
    back_a = models.TextField()
    created_at = models.DateTimeField(auto_now=True)