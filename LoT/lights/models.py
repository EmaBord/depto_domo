from django.db import models



class Light(models.Model):
	nombre 		   = models.CharField(max_length =100)
	arduino_path   = models.CharField(max_length =100)
	pin	   		   = models.IntegerField()
	estado 		   = models.BooleanField(default= False)
	



