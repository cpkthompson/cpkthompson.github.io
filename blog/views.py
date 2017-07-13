from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import BlogPost


class BlogListView(ListView):
    queryset = BlogPost.published.all()
    context_object_name = 'blog_posts'
    template_name = 'blog/list.html'


def blog_post_detail(request, post_slug):
    blog_post = get_object_or_404(BlogPost, post_slug=post_slug, post_status='published')
    return render(request, 'blog/detail.html', {'blog_post': blog_post})
