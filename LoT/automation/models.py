from django.db import models
from lights.models import Light



class Automation(models.Model):
	encendido 		   = models.CharField(max_length =100)
	apagado   		   = models.CharField(max_length =100)
	luz	   		       = models.ForeignKey(
									        Light,
									        on_delete=models.CASCADE,
									        related_name="automations",
									        related_query_name="automation",
									    )
	
