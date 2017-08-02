from django.conf.urls import url
from frontend import views

urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='HomeView'),
    url(r'^about/$', views.about, name='about'),

]
