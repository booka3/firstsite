from django.conf.urls import patterns, include, url
from firstsite.views import hello
from firstsite.views import hello2
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#	('^hello/$',hello),
#	('^hello2/$',hello2),

    # Examples:
    # url(r'^$', 'firstsite.views.home', name='home'),
    # url(r'^firstsite/', include('firstsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	url(r'^blog/', include('blog.urls')),

#    url(r'^blog2/$', 'blog.views.home', name='home'),
#    url(r'^blog2/do_task$', 'testcele.cele.views.do_task', name='do_task'),
#    url(r'^blog2/poll_state$', 'testcele.cele.views.poll_state', name='poll_state'),
#    url(r'^admin/', include(admin.site.urls)),
)
