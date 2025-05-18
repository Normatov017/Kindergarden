
from django.shortcuts import render


def servemeal_view(request):
    return render(request, 'servemeal.html')
