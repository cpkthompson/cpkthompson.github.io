from django.conf.urls import url
from frontend import views

urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='HomeView'),
    url(r'^about/$', views.AboutView.as_view(), name='AboutView'),
    url(r'^contact/$', views.ContactView.as_view(), name='ContactView'),

]
