from django.shortcuts import render
from django.contrib.auth import logout

from .forms import *

def logout(req):
	logout(req)
	return HttpResponse('logged out')
	#return render(req, 'logout.html')

def account(req):
	return HttpResponse('account')

# def login(req):
# 	form = loginForm()
# 	return render(req, 'login.html', {'form': form})
