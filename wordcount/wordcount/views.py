from django.shortcuts import render
from collections import Counter


def home(request):
    return render(request, 'home.html', {'hi': 'by ÁDÁM GYARMATI'})


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    count_of_words = len(wordlist)
    worddict = {x: wordlist.count(x) for x in wordlist}
    return render(request, 'count.html', {'fulltext': fulltext, 'count': count_of_words, 'worddict': worddict.items()})
