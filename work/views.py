from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import WorkPost


class WorkListView(ListView):
    queryset = WorkPost.published.all()
    context_object_name = 'work_posts'
    template_name = 'work/work.html'


def work_post_detail(request, post_slug):
    work_post = get_object_or_404(WorkPost, post_slug=post_slug, post_status='published')
    return render(request, 'work/work_post.html', {'work_post': work_post})
