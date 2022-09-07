from django.contrib import admin
from .models import Post,Comment,Response,Email
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Response)
admin.site.register(Email)
class PostAdmin(admin.ModelAdmin):
	list_display=['title','body','category']
	search_fields=['title','category']
	list_filter=('datetime')

class EmailAdmin(admin.ModelAdmin):
	list_display=['email']
	search_fields=['email']
	list_filter=('email')

class CommentAdmin(admin.ModelAdmin):
	list_display=['body','prenom','nom','email']
	search_fields=['prenom','email','body']
	list_filter=('datetime')


class CommentAdmin(admin.ModelAdmin):
	list_display=['body','prenom','nom','email']
	search_fields=['prenom','email','body']
	list_filter=('datetime')