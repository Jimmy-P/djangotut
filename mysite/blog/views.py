from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from .models import Post
from django.template import RequestContext
#from django.views.decorators.csrf import csrf_exempt
from .forms import MyRegistrationForm
#from django.contrib.auth.forms import UserCreationForm

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
		print "request.user", request.user.id
		users = User.objects.all()
		user = {
		      'users':users
		}

		return render(request, 'blog/create_blog.html', user)
#@csrf_exempt
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('blog/login.html', c)

#@csrf_exempt
def auth_view(request):
	print '1'
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	print '2'
	if user is not None:
		auth.login(request, user)
		return render_to_response ('blog/loggedin.html')#HttpResponseRedirect('blog/loggedin.html')
	else:
		return render_to_response ('blog/invalid.html')#HttpResponseRedirect('blog/invalid.html')

def loggedin(request):
	return render_to_response('blog/loggedin.html', {'full_name': request.user.username},
                   context_instance=RequestContext(request))

def invalid_login(request):
	return render_to_response('blog/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('blog/logout.html')

def base(request):
	return render_to_response('blog/base.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/register_success')
        
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('blog/register.html', args)

def register_success(request):
    return render_to_response('blog/register_success.html')

