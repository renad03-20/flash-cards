from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Card
from decks.models import Deck
from .forms import cardForm

@login_required
def options(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    return render(request, 'options.html', {'deck': deck})

@login_required
def add_card(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    return render(request, 'addCard.html', {'deck': deck})

@login_required
def study(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    return render(request, 'study.html', {'deck': deck})