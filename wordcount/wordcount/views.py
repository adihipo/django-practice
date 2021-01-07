from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hi': 'by ÁDÁM GYARMATI'})


def count(request):
    return render(request, 'count.html')
