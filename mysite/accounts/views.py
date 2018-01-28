from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
#from .models import Post
from django.template import RequestContext
#from django.views.decorators.csrf import csrf_exempt
#from .forms import MyRegistrationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth import login, logout


def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('accounts/login.html', c)


def auth_view(request):
	print '1'
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	print '2'
	if user is not None:
		auth.login(request, user)
		return render_to_response ('accounts/loggedin.html')#HttpResponseRedirect('blog/loggedin.html')
	else:
		return render_to_response ('accounts/invalid.html')#HttpResponseRedirect('blog/invalid.html')

def loggedin(request):
	return render_to_response('accounts/loggedin.html', {'full_name': request.user.username},
                   context_instance=RequestContext(request))

def invalid_login(request):
	return render_to_response('accounts/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('accounts/logout.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
		user = form.save()
		user.backend = 'django.contrib.auth.backends.ModelBackend'
       	return render_to_response('accounts/register_success.html')#HttpResponseRedirect('blog/register_success.html')
        
    else:
        form = UserCreationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('accounts/register.html', args)

def register_success(request):
    return render_to_response('accounts/register_success.html/')
