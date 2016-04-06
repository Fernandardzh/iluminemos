from django.contrib import admin
from .models import Blog, Coment

class 	BlogAdmin(admin.ModelAdmin):
	list_display=('title','slug','date')
	list_filter=('date')
	search_fields=('title','body')
	prepopulated_fields={'slug':('title',)}
	ordering=['date']

admin.site.register(Blog, BlogAdmin)

class ComentAdmin(admin.ModelAdmin):
	list_display=('blog','date')
	search_fields=('body',)

admin.site.register(Coment, ComentAdmin)