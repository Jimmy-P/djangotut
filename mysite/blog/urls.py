from django.conf.urls import url
from . import views



urlpatterns = [
#	url(r'^post$',views.post_list),
#	
#	url(r'^base$', 'blog.views.base'),

	#url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^postblog$',views.postblog, name='postblog'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
		views.post_detail,
		name='post_detail'),
    url(r'edit_post/(?P<id>[0-9]+)/$', views.edit_post, name='edit_post'),
]
