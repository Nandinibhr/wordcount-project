from django.http  import HttpResponse
from django.shortcuts import render

def homepage(request):
     return render(request,'home.html')

def about(request):
     return render(request,'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    max = 0

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

    for word in wordlist:
        if worddictionary[word] > max:
            max = worddictionary[word]

    return render(request,'count.html',{'fulltext':fulltext , 'count': len(wordlist), 'worddictionary': worddictionary , 'max' : max})
