from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hi': 'by ÁDÁM GYARMATI'})


def count(request):
    fulltext = request.GET['fulltext']
    count_of_words = len(fulltext.split())
    return render(request, 'count.html', {'fulltext': fulltext, 'count': count_of_words})
