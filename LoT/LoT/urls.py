from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'LoT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^LoT/', include(admin.site.urls)),
     url(r'^', include('lights.urls')),
     url(r'^', include('automation.urls')),
     url(r'^', include('autenticacion.urls')),
     
]
