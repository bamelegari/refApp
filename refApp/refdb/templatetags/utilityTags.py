from django import template

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