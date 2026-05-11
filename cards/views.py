from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Card
from decks.models import Deck
from .forms import CardForm

@login_required
def options(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
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
            messages.success(request, 'Card added! Add another, or click Done to study.')          
            return redirect('add_card', deck_id=deck.id)
    else:
        form = CardForm()

    card_count = Card.objects.filter(deck=deck).count()
    return render(request, 'addCard.html', {'form': form, 'deck': deck, 'card_count': card_count})

@login_required
def study(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    card = Card.objects.filter(deck=deck)

    if not card.exists():
        messages.warning(request, "you havn't created cards yet")
        return redirect('add_card', deck_id=deck.id)

    return render(request, 'study.html', {'deck': deck, 'card':card})