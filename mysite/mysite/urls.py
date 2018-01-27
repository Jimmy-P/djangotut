from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),

#User auth urls
	url(r'^login$', 'blog.views.login'),
	url(r'^auth$', 'blog.views.auth_view'),
	url(r'^logout$', 'blog.views.logout'),
	url(r'^loggedin$', 'blog.views.loggedin'),
	url(r'^invalid$', 'blog.views.invalid_login'),
	url(r'^register/$', 'blog.views.register_user'),
	url(r'^register_success/$', 'blog.views.register_success'),
	#url(r'^register/blog/register', 'blog.views.register_success'),


]
