from django.views.generic import ListView
from work.models import WorkPost
from django.shortcuts import render

class HomeView(ListView):
    queryset = WorkPost.published.all()[:3]
    context_object_name = 'work_posts'
    template_name = 'frontend/index.html'

def about(request):
    return render(request, "frontend/about.html", {}) 