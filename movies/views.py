from django.shortcuts import render
import requests
from random import *
# Create your views here.


def index(request):
    return render(request, 'index.html')

    
BASE_URL = 'https://api.themoviedb.org/3'
path = f'/movie/278/recommendations'
params = {
    'api_key' : 'e6fcccc78c4a58a99e1758d30d821e54',
    'language' : 'ko'
}

response = requests.get(BASE_URL + path, params=params)
data = response.json()

def recommendations(request):
    x = randint(1, int(len(data["results"])))
    context = {
        'title' : data["results"][x].get("title"),
        'poster_path' : data["results"][x].get("poster_path"), 
        'id': data["results"][x].get("id"),
        'overview': data["results"][x].get("overview"),
        'release_data': data["results"][x].get("release_date"),
        'vote_average': data["results"][x].get("vote_average"),
    }
    return render(request, 'recommendations.html', context)