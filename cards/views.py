from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Card
from decks.models import Deck
from .forms import CardForm

@login_required
def options(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    return render(request, 'options.html', {'deck': deck})

@login_required
def add_card(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.deck = deck
            card.save()
            messages.success(request, f'cards are added now you can study them!')           
            return redirect('study', deck_id=deck.id)
    else:
        form = CardForm()
        
    return render(request, 'options.html', {'form': form, 'deck': deck})

@login_required
def study(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    return render(request, 'study.html', {'deck': deck})