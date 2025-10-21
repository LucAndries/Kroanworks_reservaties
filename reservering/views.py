from django.shortcuts import render

def kalender(request):
    return render(request, 'reservering/kalender.html')

def reservering_formulier(request):
    return render(request, 'reservering/reservering_formulier.html')
