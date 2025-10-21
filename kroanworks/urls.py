from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('reservering/', include('reservering.urls')),  # Reservering app URL's
    path('kalender/', include('reservering.urls')),  # Kalender app URL's
]
