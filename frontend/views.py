from django.views.generic import ListView
from blog.models import BlogPost


class HomeView(ListView):
    queryset = BlogPost.published.all()
    context_object_name = 'posts'
    template_name = 'frontend/index.html'
