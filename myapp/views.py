from django.shortcuts import render  # type:ignore
from django.http import HttpResponse  # type:ignore
# from myapp.template import 'hello.html'


def hello(request):
    text = '<h1>Welcome to my app!</h1>'
    return HttpResponse(text)


def morning(request):
    text = '<h1>Welcome in the morning!</h1>'
    return HttpResponse(text)


def helo(request):
    return render(request, 'templates/hello.html', {})
