from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('', include('pwa.urls')),  
    url(r'^admin/', admin.site.urls),
    url(r'^', include('frontend.urls', namespace='frontend', app_name='frontend')),
    url(r'^work/', include('work.urls', namespace='work', app_name='work')),

]
