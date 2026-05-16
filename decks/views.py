from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Deck
from .forms import DeckForm

@login_required
def home_page(request):
    all_deck = Deck.objects.filter(user=request.user)
    return render(request, 'homepage.html', {'all_deck': all_deck})


@login_required
def create_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            new_deck = form.save(commit=False)
            new_deck.user = request.user
            new_deck.save()
            return redirect('Decks')
    else:
        form = DeckForm()

    return render(request, 'createDeck.html', {'form': form})


@login_required
def delete_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)

    if request.method == 'POST':
        deck.delete()
        return redirect('Decks')
    else:
        return render(request, 'deleteDeck.html', {'deck': deck})