from django.shortcuts import render
from django.http import HttpResponse


def helloworld(request):
    text = HttpResponse('hello world')
    return text


def helloworld2(request):
    return render(request, 'hello.html')


def toppage(request):
    ctx = {
    }
    return render(request, 'toppage.html', ctx)

