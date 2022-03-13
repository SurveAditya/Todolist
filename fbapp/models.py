from django.db import models

class EnModel(models.Model):
	name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	enq_msg=models.CharField(max_length=30,default="")

	def __str__(self):
		return self.name
