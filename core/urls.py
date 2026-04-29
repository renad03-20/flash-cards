from django.contrib import admin
from django.urls import path, include
from accounts import views as user_view
from django.contrib.auth import views as auth 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('decks.urls')),
    path('accounts/', include('accounts.urls')),
    path('login/', user_view.login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='accounts/index.html'), name ='logout'),
    path('register/', user_view.register, name='register'),
]