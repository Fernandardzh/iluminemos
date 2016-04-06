from django import forms
from .models import Blog, Coment

class BlogForm(forms.ModelForm):
	class Meta:
		model=Blog
		fields=('title','body')

class ComentForm(forms.ModelForm):
	class Meta:
		model=Coment
		fields=('body',)