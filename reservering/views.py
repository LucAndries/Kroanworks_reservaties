from django.shortcuts import render
from .forms import ReserveringForm

def reservering_formulier(request):
    if request.method == 'POST':
        form = ReserveringForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bevestiging.html')  # Bevestiging na succesvolle reservering
    else:
        form = ReserveringForm()
    return render(request, 'reservering_formulier.html', {'form': form})

def kalender(request):
    return render(request, 'kalender.html')  # Je kalenderpagina
