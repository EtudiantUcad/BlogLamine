from django import forms
from .models import Comment,Response,Email

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['prenom','nom','email','body']


class ResponseForm(forms.ModelForm):
	class Meta:
		model=Response
		fields=['prenom','nom','email','body']


class EmailForm(forms.ModelForm):
	class Meta:
		model=Email
		fields=['email']

class CommentForm1(forms.Form):
	name = forms.CharField(max_length=100,help_text='Your Full Name')
	email = forms.EmailField(max_length=100, help_text='Your email')
	file = forms.FileField(required=False , help_text='file')
	message=forms.CharField(widget=forms.Textarea(), help_text='Votre Message')
	class Meta:
		fields = ['name', 'email','file','message']
		 
