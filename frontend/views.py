from django.views.generic import ListView
from blog.models import BlogPost


class HomeView(ListView):
    queryset = BlogPost.published.all()[:3]
    context_object_name = 'blog_posts'
    template_name = 'frontend/index.html'


class AboutView(ListView):
    model = BlogPost
    template_name = 'frontend/about.html'


class ContactView(ListView):
    model = BlogPost
    template_name = 'frontend/contact.html'
