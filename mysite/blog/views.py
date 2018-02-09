from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from .models import Post, Comment
from django.template import RequestContext
#from django.views.decorators.csrf import csrf_exempt
#from .forms import MyRegistrationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth import login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.template.defaultfilters import slugify

#Prints the 10 first objects in the list
#def post_list(request):
#	posts = Post.objects.all()[:10]
#
#	context = {
#		'posts':posts
#	}
#
#	return render(request, 'blog/base2.html', context)

#Retrieve all posts with "published" status
def post_list(request):
    object_list = Post.published.all()#[:10]
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #If page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page,
                                                   'posts': posts})
#Displays all posts with status published,max 3 per page
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

#Takes year, month and day parameters to retrieve a post by specific date and slug
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)

    #Comments list for this post
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        #Comment was posted
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            #Create comment object but dont save to DB yet
            new_comment = comment_form.save(commit=False)
            #Assign currnt post to comment
            new_comment.post = post
            #Save comment to db
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'comments': comments,
                                                     'comment_form': comment_form})

def post_share(request, post_id):
    #retrieve post by ID
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        #Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #form fields passed validatoin
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


#adds a new Post object using title, author and body
def postblog(request):

    if(request.method == 'POST'):
        print "request.POST", request.POST
        title = request.POST['title']
        slug = request.POST['slug']
        author = request.POST['author']#request.user.get_username()
        body = request.POST['body']
        u = User.objects.get(id=int(author))	 ##NEEDFIX		
        post = Post(title=title, author=u, body=body, slug=title)#author=u, body=body,)
        post.status = 'published'
        post.save()

        return redirect('/blog')#return render(request, 'blog/post_blog.html')
    else:
		print "request.user", request.user.id
		users = User.objects.all()
		user = {
		      'users':users
		}

		return render(request, 'blog/post_blog.html')
#
#def base(request):
#	return render_to_response('blog/base.html')

