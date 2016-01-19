from multiprocessing import Process
from datetime import datetime
import time
"""
start and end we are string format date and hour: AAAA-MM-DD HH:mm
"""
class Task(Process):		
	def __init__(self,ejecute,start_up ,end ):
		Process.__init__(self) 
		self.start_up 		= start_up
		self.end   		= end
		self.ejecute 	= ejecute
		print "creado ..."

	def run(self):		
		print "comenzando ..."
		while not self.begin():		
			time.sleep(1)
		self.ejecute.action()
		while not self.final():
			time.sleep(1)
		self.ejecute.stop()
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
"""
	
tas = Task(5,'2016-01-18 18:20','2016-01-18 18:21')	

tas.start()
raw_input()
tas.terminate()
		
		
"""
