from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget

class gameAssignmentForm(forms.ModelForm):
	class Meta:
		model = Game
		exclude= ['assignor', 'assessor_notes', 'ref_comments',
			'age_group', 'level', 'gender']

class refAssignmentForm(forms.ModelForm):

	class Meta:
		model = GameHasReferee
		fields = ['referee', 'position', 'game']
		widgets = {'game': forms.HiddenInput()}


	def __init__(self, *args,**kwargs):
		context = super (refAssignmentForm,self ).__init__(*args,**kwargs)
		self.fields['referee'].queryset = Person.objects.filter(groups__name='referee')