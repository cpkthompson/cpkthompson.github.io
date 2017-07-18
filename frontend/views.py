from django.views.generic import ListView
from blog.models import BlogPost
from django.shortcuts import render

class HomeView(ListView):
    queryset = BlogPost.published.all()[:3]
    context_object_name = 'blog_posts'
    template_name = 'frontend/index.html'

def contact(request):
    return render(request, "frontend/contact.html", {}) 

def about(request):
    return render(request, "frontend/about.html", {}) 