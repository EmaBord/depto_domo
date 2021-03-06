from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from lights.models import Light
from models import Automation
from helpers.task import Task
from lights.wrapper import WrapperLight
from django.conf import settings


TEMPLATE_NEW = "automation/new.html"
class AutomationView(TemplateView):
    template_get          	  	= 'automation/get.html'   
    template_new          	  	= 'automation/new.html'   
    template_modify            	= 'automation/modify.html' 
    #template_modify_staff       = 'lights/modify_staff.html'      
    
  
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AutomationView, self).dispatch(*args, **kwargs)
 
    

    def get(self, request, *args, **kwargs):  

        update_id  =kwargs.get('update_id')
        delete_id  =kwargs.get('delete_id')
        
        if update_id:
            automation = Automation.objects.filter(pk = int(update_id))[0]
            return render(request, self.template_modify,{'automation':automation})
        elif delete_id:
            automation = Automation.objects.filter(pk = int(delete_id))[0]
            try:
                settings.TASKS[automation.id].terminate()
            except:
                    print "no existe la tarea en ram"
            try:    
                automation.estado = "parado"
                automation.save()
                try:
                    automation.luz.estado = False
                    automation.luz.save()
                except:
                    print "se rompe"
            except Exception, e:
                print str(e) + "por aca"
            #automation.delete()
        automations = Automation.objects.all()
        context = {'automations':automations}        
        return render(request, self.template_get,context)
    
      
    def post(self, request, *args, **kwargs):
    	if "modify" in request.POST:
    		return self.modify(request)       
        elif "new" in request.POST:
            return self.new(request)  
    

    def new(self,request):

        context = {}
        encendido   = request.POST.get("encendido")
        apagado     = request.POST.get("apagado")
        id_luz      = request.POST.get("id_luz")
        if encendido  and apagado and id_luz:
            encendido = encendido.replace("/","-")
            apagado   = apagado.replace("/","-")
            luz = Light.objects.filter(pk=int(id_luz))[0]
            wrapperLight = WrapperLight(luz)
            encendido_db   = encendido.split("-")
            encendido_db   =  encendido_db[2].split(" ")[0]+"/"+ encendido_db[1] +"/"+ encendido_db[0] + " a las "+encendido_db[2].split(" ")[1]
            apagado_db     = apagado.split("-")
            apagado_db     = apagado_db[2].split(" ")[0]+"/"+ apagado_db[1] +"/"+ apagado_db[0] + " a las "+ apagado_db[2].split(" ")[1]
            automation = Automation.objects.create(encendido= encendido_db,apagado=apagado_db,luz=luz,estado ="esperando")
            task = Task(wrapperLight,automation,encendido,apagado)
            settings.TASKS[automation.id] = task

            task.start()

        else:
            context["msg_error"] = 1
            lights = Light.objects.all()
            context['lights'] = lights
            return render(request, self.template_new,context)   

        automations = Automation.objects.all()

        context['automations'] = automations        
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

def new(request):
    context = {}
    lights = Light.objects.all()
    context['lights'] = lights
    return render(request, TEMPLATE_NEW,context)

def estado_json(request,pk):
    import json
    estado = Automation.objects.filter(pk=pk)[0].estado
    jSon = {'estado':estado}
    data = json.dumps(jSon)
    return HttpResponse(data, content_type='application/json')

    

   
