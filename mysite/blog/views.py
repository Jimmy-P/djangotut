from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from .models import Post

#Prints the 10 first objects in the list
def post_list(request):
	posts = Post.objects.all()[:10]

	context = {
		'posts':posts
	}

	return render(request, 'blog/base2.html', context)


#adds a new object to the list using title, author and body
def createblog(request):

	if(request.method == 'POST'):
		print "request.POST", request.POST
		title = request.POST['title']
		author = request.POST['author']
		body = request.POST['body']
		u = User.objects.get(id=int(author))			
		post = Post(title=title, author=u, body=body)
		post.save()

		return redirect('/post')
	else:
		users = User.objects.all()
		user = {
		      'users':users
		}

		return render(request, 'blog/create_blog.html', user)

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('blog/login.html', c)
	

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('blog/loggedin.html')
	else:
		return HttpResponseRedirect('blog/invalid.html')

def loggedin(request):
	return render_to_response('blog/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('blog/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('blog/logout.html')
