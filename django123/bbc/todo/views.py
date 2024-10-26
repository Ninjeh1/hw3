from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'john doe',
        'title': 'article 1',
        'content': 'First post content',
        'date_posted': 'August 26, 2018',
    },
    {
        'author': 'mary smith',
        'title': 'article 2',
        'content': 'Second post content',
        'date_posted': 'August 26, 2019',
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'bbc/home.html', context)

def create(request):
    return render(request, 'bbc/create.html', {'title': 'creation'})
