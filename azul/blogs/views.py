from django.shortcuts import render, redirect, HttpResponse
from .models import Blog
from django.views.generic import View
from .forms import BlogForm, ComentForm

from django.core import serializers

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator


class BlogView(View):
	def get(self,request):
		template="blogs/todos.html"
		blogs=Blog.objects.all()
		form=BlogForm()
		context={
		'blogs':blogs,
		'form':form
		}
		return render(request,template,context)
	def blog(self, request):
		form=BlogForm(request.POST)
		form.save()
		return redirect('blogs:todos')

#class BlogDetailView(View):
#	@method_decorator(login_required(login_url = 'cuentas:login')) 
#	def get(self,request,objeto):
#		blog=Post.objects.get(pk=objeto)
#		form=ComentForm()
#		comments=blog.coments.all()
#		template="blogs/detail.html"
#		context={
#		'blog':blog,
#		'form':form,
#		'comments':comments
#		}
#		return render(request,template,context)

	def blog(self,request,objeto):
		blog=Blog.objects.get(pk=objeto)
		new_form=ComentForm(request.POST)

		if new_form.is_valid() and request.user:
			new_com=new_form.save(commit=False)
			new_com.name=request.user
			new_com.blog=blog
			new_com.save()
			messages.success(request,"Comentario agregado!")
		else:
			messages.error(request, 'Algo falló')
		return HttpResponseRedirect(reverse('blogs:detail',args=[objeto]))


class Api(View):
	def get(self,request):
		blogs=Blog.objects.all()
		data=serializers.serialize('json',blogs)
		return HttpResponse(data,content_type='application/json')