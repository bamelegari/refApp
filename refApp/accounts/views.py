from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse

from .forms import *

def logout(req):
	auth.logout(req)
	return HttpResponse('logged out')
	#return render(req, 'logout.html')

def account(req):
	return HttpResponse('account')

def denied(req):
	return render(req, 'denied.html')

# def login(req):
# 	form = loginForm()
# 	return render(req, 'login.html', {'form': form})
