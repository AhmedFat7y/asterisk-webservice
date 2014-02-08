from django.db import models
from django.db.models.query import QuerySet

# Create your models here.
class Client(models.Model):
	extension = models.CharField(max_length=3)
	phoneNumber = models.CharField(max_length=11)
	server = models.ForeignKey('Server')
	def __unicode__(self):
		return self.extension + '-' + self.phoneNumber + '-' + self.serverIP

class Server(models.Model):
	clients = QuerySet()
	ip = models.CharField(max_length=15)