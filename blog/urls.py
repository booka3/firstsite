from django.conf.urls.defaults import *
#from firstsite.blog.views import archive
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.archive, name='archive'),
	url(r'^blog2/$', 'blog.views.home', name='home'),
	url(r'^blog2/do_task$', 'blog.views.do_task', name='do_task'),
	url(r'^blog2/poll_state$', 'blog.views.poll_state', name='poll_state'),
)
