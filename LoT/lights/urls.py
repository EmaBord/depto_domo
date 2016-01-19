from django.conf.urls import patterns, url
from lights.views import LightView

urlpatterns = patterns ('LoT.lights.views',
			 url(r'lights$', LightView.as_view(), name='lights'),
			 url(r'lights/(?P<update_id>[0-9]+)/$', LightView.as_view(), name='lights-update'),
			 url(r'lights/(?P<update_staff_id>[0-9]+)/staff/$', LightView.as_view(), name='lights-update-staff'),
    		 url(r'lights/(?P<delete_id>[0-9]+)/delete/$', LightView.as_view(),  name='lights-delete'),
			 
			 
			)
