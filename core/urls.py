from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Decks app handles the root URL
    path('', include('decks.urls')),

    # Cards app
    path('cards/', include('cards.urls')),

    # Auth views — defined here so accounts.urls doesn't clash with core
    path('login/', accounts_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', accounts_views.register, name='register'),
]