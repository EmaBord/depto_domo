from multiprocessing import Process
from datetime import datetime
import time
"""
start and end we are string format date and hour: AAAA-MM-DD HH:mm
"""
class Task(Process):		
	def __init__(self,ejecute,automation,start_up ,end ):
		Process.__init__(self) 
		self.start_up 		= start_up
		self.end   		= end
		self.ejecute 	= ejecute
		self.automation = automation
		

	def run(self):		
		while not self.begin():		
			time.sleep(1)
		self.ejecute.action()
		self.automation.estado = "ejecutandose"
		self.automation.save()
		while not self.final():
			time.sleep(1)
		self.ejecute.stop()
		self.automation.estado = "finalizado"
		self.automation.save()
	def begin(self):
		now = str(datetime.now())
		if self.start_up <= now:
			return True
		return False
			
	
	def final(self):
		now = str(datetime.now())
		if self.end <= now:
			return True
		return False
	def stop(self):
		self._stop.set()
		
		


class InterfaceObject():
	def action(self):
		 raise NotImplementedError("Debe implementar el metodo action")
	def stop(self):
		 raise NotImplementedError("Debe implementar el metodo stop")

