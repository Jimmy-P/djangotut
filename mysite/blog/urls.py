from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^post$',views.post_list),
    url(r'^createblog$',views.createblog, name='createblog'),

#User auth urls
	url(r'^login$', 'blog.views.login'),
	url(r'^auth$', 'blog.views.auth_view'),
	url(r'^logout$', 'blog.views.logout'),
	url(r'^loggedin$', 'blog.views.loggedin'),
	url(r'^invalid$', 'blog.views.invalid_login'),
	url(r'^base$', 'blog.views.base'),
	url(r'^register/$', 'blog.views.register_user'),
	url(r'^register_success/$', 'blog.views.register_success'),

]
