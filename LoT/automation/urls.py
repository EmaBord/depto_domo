from django.conf.urls import patterns, url
from automation.views import AutomationView, new, estado_json


urlpatterns = patterns ('LoT.automation.views',
			
			 url(r'automation/new/$', new, name='automation-new'),
			  url(r'automation$', AutomationView.as_view(), name='automation'),
			 url(r'automation/(?P<update_id>[0-9]+)/$', AutomationView.as_view(), name='automation-update'),
			 url(r'automation/(?P<delete_id>[0-9]+)/delete/$', AutomationView.as_view(),  name='automation-delete'),
			 url(r'automation/(?P<pk>[0-9]+)/estado/$', estado_json, name='estado-json'),
			 
			 
			)
