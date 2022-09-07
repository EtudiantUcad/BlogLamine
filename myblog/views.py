
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from .models import Post
from .models import Email as pt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm,ResponseForm,CommentForm1,EmailForm
from django.core.mail import EmailMessage
from django.contrib import messages


def page_not_found_view(request, exception): 
    return render(request, 'myblog/404.html', status=404)

def Email(request):
	if request.method=='POST':
		form=EmailForm(request.POST)
		email=request.POST.get('email')
		data=pt.objects.get(email=email)
		if data!="":
			messages.error(request,"Oups!!! Vous etes deja inscrit avec cette email Merci!!!")
		else:
			form.email=email
			form.save()
			messages.success(request,"votre inscription au service mail est bien enregistrer vous recevrais des notifications de ce site merci !!!")		
		return redirect('/')


def Contact(request):
	if request.method == 'GET':
		form = CommentForm1()
	else:
		form = CommentForm1(request.POST,request.FILES)
		if form.is_valid():
			name =request.POST.get('name')
			email =request.POST.get('email')
			message = request.POST.get('message')
			email = EmailMessage(
			'Message de :' +name,
			message+"\n\n\n\n\n\n\n "+"Emetteur:"+" "+email,
			email,
			['massalylamine22@gmail.com'],
			headers={'Reply-To': email})
			if request.FILES:
				uploaded_file = request.FILES['file']
				email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
			messages.success(request,"votre message est bien envoyer a l'administrateur du site vous recevrais une reponse en moins de 24 heurs !!!!")
			email.send()
			return redirect('contact-view')

	return render(request,'myblog/Contact.html',{'form':form})

def Question(request,id):

	if request.method == 'POST':
		full_name =request.POST.get('name')
		email =request.POST.get('email')
		message = request.POST.get('message')
		post=Post.objects.get(pk=id)
		email = EmailMessage(
		post.title,
		message+"\n\n\n\n\n\n\n "+"Emetteur :"+" "+email+'\n\n\n'+'Prenom et Nom : '+full_name,
		email,
		['massalylamine22@gmail.com'],

		headers={'Reply-To': email})
		messages.success(request,"votre message est bien envoyer a l'administrateur du site vous recevrais une reponse en moins de 24 heurs !!!!")
		email.send()
		return redirect('detail-view',id)
 
def Home(request):
	comment=None
	data=Post.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(data, 3)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	return render(request,'myblog/index.html',{'data':data,'users':users,'comment':comment})

def SearchData(request):
	if request.method=='GET':
		search_data=request.GET.get('searchdata')
		if search_data:
			result=Post.objects.filter(title__icontains=search_data)
			return render(request,'myblog/search.html',{'result':result})
		else:
			return render(request,'myblog/search.html',{})
		
def Cv_view(request):
	return render(request,'myblog/cv.html',{})

def Detail(request,id):
	comment=None
	res=None
	data=Post.objects.get(pk=id)
	liste=Post.objects.filter()[:5]
	post = get_object_or_404(Post, pk=id)
	comments = post.comment.all()

	if request.method=='POST':
		form_com=CommentForm(request.POST)
		if form_com.is_valid():
			comment=form_com.save(commit=False)
			comment.post=post
			comment.save()
			return redirect('/')
	else:
		form_com=CommentForm()
		response_form=ResponseForm()

	return render(request,'myblog/detail.html',{'liste':liste,'comments':comments,'data':data,'form_com':form_com})