from django.shortcuts import render

from .forms import *


def login(req):
	form = loginForm()
	return render(req, 'login.html', {'form': form})
