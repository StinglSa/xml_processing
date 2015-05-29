from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^polls/$', 'polls.views.index'),
                       (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.details'),
                       (r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
                       (r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
