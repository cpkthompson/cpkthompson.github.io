from django.conf.urls import url, include
from frontend import views

urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='HomeView'),

]
