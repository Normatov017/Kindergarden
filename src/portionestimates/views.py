
from django.shortcuts import render


def portionestimates_view(request):
    return render(request, 'portionestimate.html')
