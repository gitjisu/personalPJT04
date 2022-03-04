from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    return render(request, 'index.html')

def recommendations(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    # https://api.themoviedb.org/3.movie/popualr?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko&region=KR
    path = '/movie/{movie_id}/recommendations'
    params = {
        'api_key' : 'e6fcccc78c4a58a99e1758d30d821e54',
        'language' : 'ko',
        'ragion' : 'KR',
        'movie_id' : 
    }

    response = requests.get(BASE_URL+path, params=params)
    data = response.json
    print(data)
    context = {
        'data' : data
    }
    return render(request, 'recommendations.html', context )

