from django.conf.urls import url
from work import views

urlpatterns = [
    url(r'^$', views.works, name='WorkListView'),

]
