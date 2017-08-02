from django.conf.urls import url
from work import views

urlpatterns = [
    url(r'^$', views.WorkListView.as_view(), name='WorkListView'),
    url(r'^(?P<post_slug>[-\w]+)/$', views.work_post_detail, name='work_post_detail'),

]
