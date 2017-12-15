from django.shortcuts import render
from django.http import HttpResponse

def home(req):

	return render(req, 'home.html')

def reports(req):
	return HttpResponse('reports')

def stats(req):
	return HttpResponse('stats')

def referees(req):
	return HttpResponse('referees')