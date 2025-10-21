from django.shortcuts import render, redirect
from .forms import ReserveringForm

def reservering_formulier(request):
    if request.method == 'POST':
        form = ReserveringForm(request.POST)
        if form.is_valid():
            reservering = form.save()  # Sla de reservering op in de database
            return redirect('bevestiging')  # Redirect naar de bevestigingspagina
    else:
        form = ReserveringForm()

    return render(request, 'reservering_formulier.html', {'form': form})


def bevestiging(request):
    return render(request, 'bevestiging.html')  # Render het bevestigingstemplate
