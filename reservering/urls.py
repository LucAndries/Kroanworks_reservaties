from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.reservering_formulier, name='reservering_formulier'),
    path('bevestiging/', views.bevestiging, name='bevestiging'),  # Bevestigingspagina
]
