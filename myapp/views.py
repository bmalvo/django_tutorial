from django.shortcuts import render  # type:ignore
from django.http import HttpResponse  # type:ignore


def hello(request):
    text = '<h1>Welcome to my app!</h1>'
    return HttpResponse(text)


def helo(request):
    return render(request, 'myapp/template/hello.html', {})
