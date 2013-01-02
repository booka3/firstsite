from django.conf.urls.defaults import *
#from firstsite.blog.views import archive
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.archive, name='archive'),
)
