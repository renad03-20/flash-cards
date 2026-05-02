from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login   
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            try:
                htmly = get_template('Email.html')
                html_content = htmly.render({'username': username})
                subject = 'Welcome to FlashCards!'
                from_email = settings.EMAIL_HOST_USER
                msg = EmailMultiAlternatives(subject, html_content, from_email, [email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except Exception:
                pass  

            messages.success(request, f'Account created! You can now log in.')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form, 'title': 'Sign Up'})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('Decks')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'Log In'})