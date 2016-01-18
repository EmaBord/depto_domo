from django.conf.urls import patterns, url
from lights.views import LightView

urlpatterns = patterns ('LoT.lights.views',
			 url(r'lights$', LightView.as_view(), name='lights'),
			 url(r'lights/new$', LightView.as_view(), name='add_light'),
			 
			 
			)
