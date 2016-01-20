from django.conf.urls import patterns, url
from autenticacion.views import login,logout
urlpatterns = patterns ('recruiting.asignacion.views',
			
			 url(r'login$',login, name='login'),
			 url(r'logout$',logout, name='logout'),
			 url(r'accounts/login/$', login, name='login'),
			 url(r'$', login, name='login'),
			 
			 
			)