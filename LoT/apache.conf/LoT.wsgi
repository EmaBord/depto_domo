import os, sys
PATH_PROJECT = "/home/midas/Escritorio/domotica/depto_domo/"
sys.path.insert(0,PATH_PROJECT +'/lib/python2.7/site-packages')
sys.path.insert(0,PATH_PROJECT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'LoT.settings'
from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()
def application(environ, start_response):
  environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
  if environ['wsgi.url_scheme'] == 'https':
    environ['HTTPS'] = 'on'
  return _application(environ, start_response)

