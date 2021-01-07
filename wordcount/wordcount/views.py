from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'hi': 'by ÁDÁM GYARMATI'})


def about(request):
    return render(request, 'about.html', {'hi': 'by ÁDÁM GYARMATI'})


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    count_of_words = len(wordlist)
    worddict = {x: wordlist.count(x) for x in wordlist}
    sorteddict = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': count_of_words, 'sorteddict': sorteddict})
