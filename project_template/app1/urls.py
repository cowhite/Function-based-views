#Basic urls structure for an app in a Django project

from django.conf.urls import patterns, include, url

urlpatterns = patterns('app1.views',
	url(r'^http_response/$', 'http_response', name='http_response'),
)