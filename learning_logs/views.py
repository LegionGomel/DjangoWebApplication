from django.shortcuts import render

# Create your views here.


def index(request):
    """Homepage of Learning Log app"""
    return render(request, 'learning_logs/index.html')
