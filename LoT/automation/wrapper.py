from django.conf import settings

class WrapperLight():
	def __init__(self,light):
		self.light = light
	def action(self):
		try:
			settings.ARDUINOS[self.light.arduino_path].digitalWriteUp(self.light.pin)
		except Exception,e:
			print str(e)
	def stop(self):
		try:
			settings.ARDUINOS[self.light.arduino_path].digitalWriteDown(self.light.pin)
		except Exception,e:
			print str(e)
            
      
		
