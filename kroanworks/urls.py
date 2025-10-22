from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simpele homepage — wordt getoond op hoofddomein
def home(request):
    return HttpResponse("<h2>Welkom bij Kroanworks Reservaties</h2><p>Gebruik /reservering of /kalender in de URL.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # ✅ nieuwe hoofdpagina
    path('reservering/', include('reservering.urls')),
    path('kalender/', include('reservering.urls')),
]
