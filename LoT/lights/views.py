from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from models import Light
from wrapper import WrapperLight



class LightView(TemplateView):
    template_get          	  	= 'lights/get.html'   
    template_modify            	= 'lights/modify.html' 
    template_modify_staff       = 'lights/modify_staff.html'      
    
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LightsView, self).dispatch(*args, **kwargs)
    """
    

    def get(self, request, *args, **kwargs):  

        update_id  =kwargs.get('update_id')
        update_staff_id  =kwargs.get('update_staff_id')
        delete_id  =kwargs.get('delete_id')
        
        if update_id:
            light = Light.objects.filter(pk = int(update_id))[0]
            return render(request, self.template_modify,{'light':light})
        elif delete_id:
            light = Light.objects.filter(pk = int(delete_id))[0]
            light.delete()
        elif update_staff_id:
            light = Light.objects.filter(pk = int(update_staff_id))[0]
            return render(request, self.template_modify_staff,{'light':light})

        lights = Light.objects.all()
        context = {'lights':lights}        
        return render(request, self.template_get,context)
    
      
    def post(self, request, *args, **kwargs):
    	if "action" in request.POST:
    		return self.action(request)
    	elif "modify" in request.POST:
    		return self.modify(request)
        elif "modify_staff" in request.POST:
            return self.modify_staff(request) 
        elif "new" in request.POST:
            return self.new(request)  
    def new(self,request):
        nombre         = request.POST.get("nombre")
        arduino_path   = request.POST.get("arduino_path")
        pin            = request.POST.get("pin")
        Light.objects.create(nombre = nombre,arduino_path = arduino_path,pin = pin)
        lights = Light.objects.all()

        context = {'lights':lights}        
        return render(request, self.template_get,context)        




    def modify(self,request):
    	idl			   = int(request.POST.get("idl"))
    	nombre 		   = request.POST.get("nombre")
    	arduino_path   = request.POST.get("arduino_path")
    	pin	   		   = request.POST.get("pin")
    	light 		   = Light.objects.filter(pk = idl)
    	light.update(nombre = nombre,arduino_path = arduino_path,pin = pin)
    	lights = Light.objects.all()
    	context = {'lights':lights}        
    	return render(request, self.template_get,context)


    def modify_staff(self,request):
        idl            = int(request.POST.get("idl"))
        nombre         = request.POST.get("nombre")
        # quedrme con el nombre del icono
        light          = Light.objects.filter(pk = idl)
        light.update(nombre = nombre)
        lights = Light.objects.all()
        context = {'lights':lights}        
        return render(request, self.template_get,context)

    def action(self,request):
    	idl			   = int(request.POST.get("ida"))
    	light 		   = Light.objects.filter(pk = idl)
    	estado 		   = light[0].estado
    	estado 		   = not estado
        wrapper        = WrapperLight(light[0])
        if estado:
            wrapper.action()
        else:
            wrapper.stop()
        light.update(estado = estado)        
    	lights 		   = Light.objects.all()
    	context 	   = {'lights':lights}        
    	return render(request, self.template_get,context)
