from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from models import Light



class LightView(TemplateView):
    template_get          	  	= 'lights/get.html'   
    template_new            	= 'lights/new.html'
    template_modify            	= 'lights/modify.html'      
    
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LightsView, self).dispatch(*args, **kwargs)
    """
    

    def get(self, request, *args, **kwargs):
    	lights = Light.objects.all()
        context = {'lights':lights}    

        return render(request, self.template_get,context)
    
      
    def post(self, request, *args, **kwargs):
    	if "new" in request.POST:
    		return self.new(request)
    	elif "action" in request.POST:
    		return self.action(request)
    	elif "modify" in request.POST:
    		return self.modify(request)    	
    	

    def new(self,request):
    	nombre 		   = request.POST.get("nombre")
    	arduino_path   = request.POST.get("arduino_path")
    	pin	   		   = request.POST.get("pin")
    	Light.objects.create(nombre = nombre,arduino_path = arduino_path,pin = pin)
    	lights = Light.objects.all()

    	context = {'lights':lights}        
    	return render(request, self.template_get,context)

    def modify(self,request):
    	idl			   = int(request.POST.get("idl"))
    	nombre 		   = request.POST.get("nombre")
    	arduino_path   = request.POST.get("arduino_path")
    	pin	   		   = request.POST.get("pin")
    	light 		   = Light.objects.filter(pk = idl)[0]
    	light.update(nombre = nombre,arduino_path = arduino_path,pin = pin)
    	lights = Light.objects.all()
    	context = {'lights':lights}        
    	return render(request, self.template_get,context)

    def action(self,request):
    	idl			   = int(request.POST.get("idl"))
    	light 		   = Light.objects.filter(pk = idl)[0]
    	estado 		   = light.estado
    	estado 		   = not estado
    	light.update(estado = estado)
    	lights 		   = Light.objects.all()
    	context 	   = {'lights':lights}        
    	return render(request, self.template_get,context)
