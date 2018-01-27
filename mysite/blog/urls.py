from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^post$',views.post_list),
    url(r'^createblog$',views.createblog, name='createblog'),
	url(r'^base$', 'blog.views.base'),


]
