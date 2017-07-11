from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.template import RequestContext

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^polls/', include('polls.urls')),
	url(r'^built/', include('env_issues.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	# r171
	url(r'^about/$', direct_to_template, {'template': 'env_issues/aboutUs.html'}),
	url(r'^$', direct_to_template, {'template': 'env_issues/index.html'}),
	url(r'^SupportiveRTC_TH/$', direct_to_template, {'template': 'env_issues/SupportiveRTC_TH.html'}),
	url(r'^SupportiveRTC_W/$', direct_to_template, {'template': 'env_issues/SupportiveRTC_W.html'}),
	url(r'^SupportiveRTC_Comparison/$', direct_to_template, {'template': 'env_issues/SupportiveRTC_Comparison.html'}),
	url(r'^application/$', direct_to_template, {'template': 'env_issues/application.html'}),
	url(r'^analysis/$', direct_to_template, {'template': 'env_issues/analysis.html'}),
	url(r'disclaimer/$', direct_to_template, {'template': 'env_issues/disclaimer.html'}),
	
)
