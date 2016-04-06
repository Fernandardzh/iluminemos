from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class Blog(models.Model):
	title=models.CharField()
	slug=models.SlugField(max_length=50, blank=True,null=True)
	body=models.TextField()
	date=models.DateTimeField(auto_now=True)
	#autor=models.ForeignKey(User,related_name='blogs_publicados',blank=True,null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogs:detail',args=[self.pk])


class Coment(models.Model):
	blog=models.ForeignKey(Post,related_name='coments',blank=True,null=True)
	body=models.TextField(null=True,blank=True)
	#name=models.ForeignKey(User,related_name='autor',blank=True,null=True)
	date=models.DateTimeField(auto_now=True,blank=True,null=True)

	#def __str__(self):
	#	return 'comentario de {} en {}'.format(self.name,self.post)


