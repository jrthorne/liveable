##################################################################
FileName		= 'urls.py'
# By:			Jason Thorne
# Date:			11-03-2012
# Description: 	The env_issues project
##################################################################
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template
from env_issues.models import Session, LinkAudit
import env_issues.views as views

# DetailView.as_view(
#			model=Session,
#			template_name='env_issues/dynamic-map.html'))
urlpatterns = patterns('',
	# r171 had to change index.html to listofsessions.html
	url(r'/listofsessions/^$', 
		ListView.as_view(
			queryset=Session.objects.order_by('-start'),
			context_object_name='SessionList',
			template_name='env_issues/listofsessions.html')),
	
	# Register a user. Create participant if DNE, create a session if DNE, and return the session id.
	# the user id is their email address. This regex works pretty well with email.
	
	# I updated this to allow for a json string of user attributes to be passed by dictionary
	# original email match is commented in line underneath
	url(r'^register/(?P<jsonUser>[^\{]*(\{[^\}]+\})[^}]*)/$', views.register),
	# r166
	url(r'^registrationFields/$', views.registrationFields),
	
	# r213 web registration
	url(r'webregister/', views.webregister),
	
	#url(r'^register/(?P<userEmail>[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})/([a-zA-Z0-9._%+-]+)/$', \
	#	views.register), 
	
	# add an audit
	url(r'^audit/(?P<jsonAudit>[^\{]*(\{[^\}]+\})[^}]*)/$', views.audit),
	url(r'^map/(?P<sessionId>\d+)/$', views.showmap),
	# r203
	url(r'^objectMap/(?P<sessionId>\d+)/$', views.showObjectmap),
	# r130 added functionality for map
	url(r'^loginMap/$', views.login),
	url(r'^loginFB/$', views.feedback),
	# r197
	url(r'^loginObject/$', views.loginObject),
	
	# r190
	#url(r'^audit/(?P<auditType>[a-z,A-Z]+)/(?P<auditID>\d+)/$', views.editAudit),
	# r197
	#url(r'^object/(?P<objectType>[a-z,A-Z]+)/(?P<objectID>\d+)/$', views.editObject),
	url(r'^objects/(?P<sessionId>\d+)/$', views.objectListReport),
	
	#url(r'^login/(?P<userEmail>[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})/([a-zA-Z0-9._%+-]+)/$', \
		#views.register),
	# r142	
	url(r'^singleUserLogin/(?P<jsonUser>[^\{]*(\{[^\}]+\})[^}]*)/$', views.singleUserLogin),
	
	# r144
	url(r'^retCloseObjects/(?P<jsonParms>[^\{]*(\{[^\}]+\})[^}]*)/$', views.retCloseObjects),
	# r179
	url(r'^showCloseAudits/(?P<jsonParms>[^\{]*(\{[^\}]+\})[^}]*)/$', views.showCloseAudits),
		
	# r131
	url(r'^feedback/$', views.feedback),
	
	# r148
	url(r'^listTypes/(?P<jsonParms>[^\{]*(\{[^\}]+\})[^}]*)/$', views.listTypes),
	# r149
	url(r'^newObject/(?P<jsonParms>[^\{]*(\{[^\}]+\})[^}]*)/$', views.newObject),
	#url(r'^upload/$', views.upload),
	
	# reportlab PDF generation
	url(r'^(?P<sessionId>\d+)/auditListReportPDF/$', views.auditListReportPDF), 
	url(r'^(?P<sessionId>\d+)/$', views.auditListReport),
	#url(r'^(?P<pk>\d+)/$', 
	#	DetailView.as_view(
	#		model=Session,
	#		template_name='env_issues/audits.html')),
	
	url(r'^getMessage/(?P<msgID>[a-z,A-Z,0-9,\_]+)/$', views.getMessage),
	
	# testing email 
	url(r'^testEmail/$', views.testEmail), 
	# converting warringah files
	#url(r'^convWar/$', views.convWar),
	
)
