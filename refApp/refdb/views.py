from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(req):

	return render(req, 'home.html')

@login_required
def reports(req):
	return HttpResponse('reports')

@login_required
def stats(req):
	return HttpResponse('stats')

@login_required
def referees(req):
	return HttpResponse('referees')