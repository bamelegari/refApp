from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group

register = template.Library()

#def getUserObjectbyName(uname):
#   return User.objects.get(username=uname)

@register.filter
def is_ref(user):
	return user.groups.filter(name='referee').exists()

@register.filter
def is_assignor(user):
	return user.groups.filter(name='assignor').exists()

@register.filter
def is_assessor(user):
	return user.groups.filter(name='assessor').exists()

@register.filter
def is_instructor(user):
	return user.groups.filter(name='instructor').exists()

@register.filter
def is_administrator(user):
	return user.groups.filter(name='administrator').exists()






@login_required
def home(req):

	return render(req, 'home.html')

@login_required
def stats(req):
	return HttpResponse('stats')

@login_required
def referees(req):
	return HttpResponse('referees')

@user_passes_test(is_ref, login_url='/denied/', redirect_field_name=None)
def reports(req):
	return HttpResponse('reports')

@user_passes_test(is_ref, login_url='/denied/', redirect_field_name=None)
def assignments(req):
	return HttpResponse('assignments')

@user_passes_test(is_assignor, login_url='/denied/', redirect_field_name=None)
def assign(req):
	return HttpResponse('assign')

@user_passes_test(is_instructor, login_url='/denied/', redirect_field_name=None)
def testscores(req):
	return HttpResponse('test scores')

@user_passes_test(is_administrator, login_url='/denied/', redirect_field_name=None)
def adduser(req):
	return HttpResponse('add user')

@user_passes_test(is_assessor, login_url='/denied/', redirect_field_name=None)
def assess(req):
	return HttpResponse('assess')