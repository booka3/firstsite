from django.conf.urls.defaults import *
#from firstsite.blog.views import archive
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.archive, name='archive'),
    url(r'^(blog2)/$', 'views.home', name='home'),
#	url(r'^(blog2)/$', 'blog.testcele.cele.views.home', name='home'),
    url(r'^(blog2)/do_task$', 'testcele.cele.views.do_task', name='do_task'),
    url(r'^(blog2)/poll_state$', 'testcele.cele.views.poll_state', name='poll_state'),
)
