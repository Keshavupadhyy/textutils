#i have create this file = keshavf
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("hello django")
#
# def about(request):
#     return HttpResponse("about hello django")
#
# def facebook(request):
#     return HttpResponse('''<a href="https://www.facebook.com/watch/?ref=tab">facebook</a>''')
#
# def mail(request):
#     return HttpResponse('''<a href="https://accounts.google.com/b/0/AddMailService">mail</a>''')
#
# def tweet(request):
#     return HttpResponse('''<a href="https://twitter.com/explore">tweet</a>''')

def index(request):

    return  render(request, 'index.html', )
    #return HttpResponse("Home")

def removepunc(request):
    #get the text and anlyze the text
    print(request.GET.get('text', 'default'))
    return HttpResponse("remove punc")

def capitalizefirst(request):
    return HttpResponse("capit alize first")

def newlineremove(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000/newlineremove">newline</a>''')

def spaceremover(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000/spaceremover">spaceremove</a>''')


def charcount(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000/charcount">charcount</a>''')

