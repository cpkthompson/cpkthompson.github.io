from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name='BlogListView'),
    url(r'^(?P<post_slug>[-\w]+)/$', views.blog_post_detail, name='blog_post_detail'),

]
