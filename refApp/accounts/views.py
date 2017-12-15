from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse

def logout(req):
	auth.logout(req)
	return render(req, 'logout.html')
	#return render(req, 'logout.html')

def account(req):
	return HttpResponse('account')

def denied(req):
	return render(req, 'denied.html')