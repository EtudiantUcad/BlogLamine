from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
	choices = [
	('django','django'),
    ('python', 'python'),
    ('html', 'html'),
    ('java', 'java'),
    ('css', 'css'),
    ('bootstrap', 'bootstrap'),
    ('annonce','annonce')
]
	title=models.CharField(max_length=100)
	category=models.CharField(choices=choices , default='django',max_length=100)
	body=RichTextField(default='')
	datetime=models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table='Post'
		ordering=["-datetime"]

	def __str__(self):
		return self.title


class Email(models.Model):
	email=models.EmailField(max_length=1000)
	class Meta:
		db_table='email'
	def __str__(self):
		return self.email


class Comment(models.Model):
	post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')
	prenom=models.CharField(max_length=100)
	nom=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	body=models.TextField(max_length=100)
	datetime=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['-datetime']
	def __str__(self):
		return self.body


class Response(models.Model):
	comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='comment_reponse')
	prenom=models.CharField(max_length=100)
	nom=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	body=models.TextField(max_length=10000)
	datetime=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['-datetime']
	def __str__(self):
		return self.body