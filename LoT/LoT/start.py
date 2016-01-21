from automation.models import Automation
from lights.models import Light
from lights.wrapper import WrapperLight
from helpers.arduino import Arduino
from helpers.task import Task
from django.conf import settings
from datetime import datetime


def run():
	automations_ejecutandose 	= Automation.objects.filter(estado = "ejecutandose")
	automations_esperando 		= Automation.objects.filter(estado = "esperando")
	lights						= Light.objects.all()
	automation = ''
	for automation in automations_esperando:
		if automation != '':
			wrapperLight = WrapperLight(automation.luz)
	    	s = automation.encendido
	    	encendido = s.split(" a las")[0].split("/")[2]+"-"+s.split(" a las")[0].split("/")[1]+"-"+s.split(" a las")[0].split("/")[0]+s.split(" a las")[1]
	    	apagado   = automation.apagado.split(" a las")[0].split("/")[2]+"-"+automation.apagado.split(" a las")[0].split("/")[1]+"-"+automation.apagado.split(" a las")[0].split("/")[0]+automation.apagado.split(" a las")[1]
	    	now = str(datetime.now())
	    	if now < apagado:
	    		task = Task(wrapperLight,automation,encendido,apagado)
	    		settings.TASKS[automation.id] = task
	    		task.start()
	    	else:
	    		wrapperLight.stop()
	    		automation.estado = "corte electrico"
	    		automation.save()





	for light in lights:
		if not light.estado:
			settings.ARDUINOS[light.arduino_path].digitalWriteDown(light.pin)
	task = ''
	for automation in automations_ejecutandose:
		wrapperLight = WrapperLight(automation.luz)
		encendido = automation.encendido.split(" a las")[0].split("/")[2]+"-"+automation.encendido.split(" a las")[0].split("/")[1]+"-"+automation.encendido.split(" a las")[0].split("/")[0]+automation.encendido.split(" a las")[1]
		apagado   = automation.apagado.split(" a las")[0].split("/")[2]+"-"+automation.apagado.split(" a las")[0].split("/")[1]+"-"+automation.apagado.split(" a las")[0].split("/")[0]+automation.apagado.split(" a las")[1]
		now = str(datetime.now())
		if now < apagado:
			task = Task(wrapperLight,automation,encendido,apagado)
			if task!='':
				settings.TASKS[automation.id] = task
				task.start()
		else:
			wrapperLight.stop()
			automation.estado = "no concluyo por corte electrico"
			automation.save()
    



