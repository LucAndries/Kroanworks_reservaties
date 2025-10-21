from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservering_formulier, name='reservering_formulier'),  # URL voor het formulier
    path('kalender/', views.kalender, name='kalender'),  # URL voor de kalender
]
