from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservering/', include('reservering.urls')),  # Zorg ervoor dat de reservering URL's worden geladen
    path('kalender/', include('reservering.urls')),  # Voeg de kalender URL's toe
]
