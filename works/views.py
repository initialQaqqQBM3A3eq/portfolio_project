from django.shortcuts import render
from django.http import HttpResponse

def portfolio(request):
    return HttpResponse("<h1>こんにちは！これは作品紹介ページです</h1>")