# from django.conf.urls import patterns, include, url
from django.urls import path
from . import views

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
#import settings

admin.autodiscover()
#media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')

urlpatterns = [
	# Examples:
	path('', views.Index, name='home'),
	path('survey/<id>/', views.SurveyDetail, name='survey_detail'),
	path('confirm/<uuid>/', views.Confirm, name='confirmation'),
	path('privacy/', views.privacy, name='privacy_statement'),


	# Uncomment the admin/doc line below to enable admin documentation:
	path('admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	path('admin/', include(admin.site.urls)),
]

# media url hackery. le sigh. 
urlpatterns += [
	
    ('%s/<path>' % media_url, 'django.views.static.serve',
     { 'document_root': settings.MEDIA_ROOT, 'show_indexes':True }),
]


'''
from django.contrib import admin
import settings

admin.autodiscover()
media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'survey.views.Index', name='home'),
	url(r'^survey/(?P<id>\d+)/$', 'survey.views.SurveyDetail', name='survey_detail'),
	url(r'^confirm/(?P<uuid>\w+)/$', 'survey.views.Confirm', name='confirmation'),
	url(r'^privacy/$', 'survey.views.privacy', name='privacy_statement'),


	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)

# media url hackery. le sigh. 
urlpatterns += patterns('',
    (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
     { 'document_root': settings.MEDIA_ROOT, 'show_indexes':True }),
)

'''