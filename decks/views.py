from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Deck
from .forms import DeckForm

@login_required
def all_deck(request):
    all_deck = Deck.objects.all()
@login_required
def create_deck(request):
    # create_deck = Deck.objects.create()
    form = DeckForm(request.POST)
    if form.is_valid():
        new_deck = form.save(commit=False)
    
        new_deck.user = request.user

        new_deck.save()
    else:
        form = DeckForm()

    context = {'form': form}
    return render(request, 'decks/templates/deck_namager.html', context)