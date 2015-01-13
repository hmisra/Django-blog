from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home','helloworld.views.home',name='home'),
    url(r'^$','helloworld.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/(?P<blog_id>\d+)/$', 'helloworld.views.blog', name="blog"),
    url(r'^blog','helloworld.views.bloghome',name='bloghome'),
)
