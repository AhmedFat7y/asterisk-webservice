import json
from django.shortcuts import render
from myapp.models import Client, Server
from django.http import HttpResponse, HttpResponseNotFound
from myapp.forms import ClientRegisteration
# Create your views here.
def register(request):
	form = ClientRegisteration(request.POST)
	if not form.is_valid():
		return HttpResponseNotFound()
	client, created = Client.objects.get_or_create(phoneNumber=form.cleaned_data['username'])	
	if created:
		client.save()
		client.extension = str(100 + client.id)
		if client.id <= 100:
			client.server = 1
		else:
			client.server = 2
		client.save()
	return HttpResponse("%s,%s" % (client.extension, client.server.ip))

def exist(request, phones):
	clients = Client.objects.filter(phoneNumber__in=phones)
	if not clients.exists():
		return HttpResponseNotFound()
	jsonData = []
	for client in clients:
		jsonData.append({
			'phone': client.phone,
			'extension': client.extension,
			'serverIp': client.server.ip,
			})
	return HttpResponse(json.dumps(jsonData), content_type="application/json")