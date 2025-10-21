from django.urls import path
from . import views

urlpatterns = [
    path('kalender/', views.kalender, name='kalender'),  # URL voor de kalenderpagina
    path('reservering/', views.reservering_formulier, name='reservering_formulier'),  # URL voor het reserveringsformulier
]
