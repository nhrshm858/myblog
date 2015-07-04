from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myapp21.views.home', name='home'),
    url(r'^about/', 'myapp21.views.about', name='about'),
	url(r'^admin/', include(admin.site.urls)),

)
