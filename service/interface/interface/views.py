from django.http import HttpResponse
from django.shortcuts import render
from django.views.static import serve
from django.views.decorators.csrf import csrf_exempt
import requests


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def mirror(request):
    response = requests.post(
        'http://flask_mirror:5000',
        {
            'text': request.POST['text']
        })
    return HttpResponse(response.json()['text'])


@csrf_exempt
def letters(request):
    response = requests.post(
        'http://flask_letters:5000',
        {
            'text': request.POST['text']
        })
    return HttpResponse(response.json()['text'])


@csrf_exempt
def words(request):
    response = requests.post(
        'http://flask_words:5000',
        {
            'text': request.POST['text']
        })
    return HttpResponse(response.json()['text'])


@csrf_exempt
def pokemon(request):
    response = requests.post(
        'http://flask_pokemon:5000',
        {
            'text': request.POST['text'],

        })
    return HttpResponse(response.json()['text'])

