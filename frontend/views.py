from django.views.generic import ListView
from work.models import WorkPost
from django.shortcuts import render


def index(request):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return render(request, "frontend/index.html", {'nums': nums})

def about(request):
    return render(request, "frontend/about.html", {}) 