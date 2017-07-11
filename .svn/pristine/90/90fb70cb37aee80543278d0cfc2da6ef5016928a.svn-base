##################################################################
FileName		= 'admin.py'
# By:			Jason Thorne
# Date:			11-03-2012
# Description: 	The env_issues project
##################################################################
from env_issues.models import Space, Link, AccessPoint, Service, \
SpaceType, LinkType, AccessPointType, ServiceType, \
SpaceStandards, LinkStandards, ServiceStandards, AccessPointStandards, \
SpaceAudit, LinkAudit, ServiceAudit, AccessPointAudit, Session, Participant, \
Feedback, ProxySpace, ProxySpaceAudit, ProxySpaceStandard, ProxySpaceType, \
ProxyLink, ProxyLinkAudit, ProxyLinkStandard, ProxyLinkType, \
ProxyAccessPoint, ProxyAccessPointAudit, ProxyAccessPointStandard, ProxyAccessPointType, \
ProxyService, ProxyServiceAudit, ProxyServiceStandard, ProxyServiceType, message
from django.contrib import admin

###############################################################
class SpaceAdmin(admin.ModelAdmin):
	fields			= ['address', 'type', 'name', 'longitude','latitude', \
					'photo', 'audio', 'score', 'properties', 'entered', 'session']
	list_display		= ('id', 'session', 'address', 'name', 'type' )
	search_fields		= ['name', 'address', 'properties']
	list_filter			= ('type','session')
# end SpaceAdmin

###############################################################
class LinkAdmin(admin.ModelAdmin):
	fields			= ['type', 'name', 'longitude','latitude', \
					'photo', 'audio', 'score', 'properties', 'entered', 'session']
	list_display		= ['id', 'session', 'name', 'type']
	search_fields		= ['name', 'properties']
	list_filter			= ('type','session')
# end LinkAdmin
###############################################################
class AccessPointAdmin(admin.ModelAdmin):
	fields			= ['type', 'name', 'longitude','latitude', \
					'photo', 'audio', 'score', 'properties', 'entered', 'session']
	list_display		= ('id', 'session', 'type', 'name')
	search_fields		= ['name', 'properties']
	list_filter			= ('type', 'session')
	
# end AccessPointAdmin
###############################################################
class ServiceAdmin(admin.ModelAdmin):
	fields			= ['type', 'name', 'longitude','latitude', \
					'photo', 'audio', 'score', 'properties', 'entered', 'session']
	list_display		= ('id', 'session', 'type', 'name')
	search_fields		= ['name', 'properties']
	list_filter			= ('type', 'session')
# end AccessPointAdmin
###############################################################
class ServiceTypeAdmin(admin.ModelAdmin):
	fields			= ['type']
	list_display	= ['id', 'type']
# end ServicePointTypeAdmin
###############################################################
class AccessPointTypeAdmin(admin.ModelAdmin):
	fields			= ['type']
	list_display	= ['id', 'type']
# end AccessPointTypeAdmin
###############################################################
class LinkTypeAdmin(admin.ModelAdmin):
	fields			= ['type']
	list_display	= ['id', 'type']
# end LinkTypeAdmin
###############################################################
class SpaceTypeAdmin(admin.ModelAdmin):
	fields			= ['type']
	list_display	= ['id', 'type']
# end SpaceTypeAdmin
###############################################################
class SpaceStandardsAdmin(admin.ModelAdmin):
	fields			= ['type', 'reference', 'element', 'criteria', 'comment', 'photo']
	list_display	= ['id', 'type', 'reference', 'element']
# end SpaceStandardsAdmin
###############################################################
class LinkStandardsAdmin(admin.ModelAdmin):
	fields			= ['type', 'reference', 'element', 'criteria', 'comment', 'photo']
	list_display	= ['id', 'type', 'reference', 'element']
# end LinkStandardsAdmin
###############################################################
class ServiceStandardsAdmin(admin.ModelAdmin):
	fields			= ['type', 'reference', 'element', 'criteria', 'comment', 'photo']
	list_display	= ['id', 'type', 'reference', 'element']
# end ServiceStandardsAdmin
###############################################################
class AccessPointStandardsAdmin(admin.ModelAdmin):
	fields			= ['type', 'reference', 'element', 'criteria', 'comment', 'photo']
	list_display	= ['id', 'type', 'reference', 'element']
# end AccessPointStandardsAdmin
###############################################################
class SpaceAuditAdmin(admin.ModelAdmin):
	fields			= ['owner', 'entered', 'standard', \
					'conforms', 'score', 'notes', 'photo', 'audio', 'session']
	list_display	= ['id', 'owner', 'session']
	list_filter		= ('session',)
	search_fields	= ['notes']
	raw_id_fields		= ('owner','session')
# end SpaceAuditAdmin
###############################################################
class LinkAuditAdmin(admin.ModelAdmin):
	fields			= ['owner', 'entered', 'standard', \
					'conforms', 'score', 'notes', 'photo', 'audio', 'session']
	list_display	= ['id', 'owner', 'session']
	list_filterq	= ('session',)
	search_fields	= ['notes']
	raw_id_fields		= ('owner','session')
# end LinkAuditAdmin
###############################################################
class ServiceAuditAdmin(admin.ModelAdmin):
	fields			= ['owner', 'entered', 'standard', \
					'conforms', 'score', 'notes', 'photo', 'audio', 'session']
	list_display	= ['id', 'owner', 'session']
	list_filter		= ('session',)
	search_fields	= ['notes']
	raw_id_fields		= ('owner','session')
# end ServiceAuditAdmin
###############################################################
class AccessPointAuditAdmin(admin.ModelAdmin):
	fields			= ['owner', 'entered', 'standard', \
					'conforms', 'score', 'notes', 'photo', 'audio', 'session']
	list_display	= ['id', 'owner', 'session']
	list_filter		= ('session',)
	search_fields	= ['notes']
	raw_id_fields		= ('owner','session')
	
	
# end AccessPointAuditAdmin
###############################################################
class ParticipantAdmin(admin.ModelAdmin):
	fields			= ['email', 'first_name', 'gender', 'organisation', \
		'suburb', 'birth_year', 'residentYears', 'comment', 'session']
	list_display	= ['id', 'first_name', 'email', 'birth_year']
	search_fields	= ['first_name', 'email', 'suburb', 'comment']
	list_filter		= ('gender', 'suburb')
	# r168
	filter_horizontal	= ['session']
# end ParticipantAdmin

###############################################################
class ParticipantSessionInline(admin.TabularInline):
	model				= Participant.session.through
	extra				= 3
# end participantInline

###############################################################
class LinkAuditInline(admin.TabularInline):
	model				= LinkAudit
	extra				= 0
	fields				= ['owner', 'entered', 'notes', 'photo', 'audio']
# end linkAuditInline

###############################################################
class ServiceAuditInline(admin.TabularInline):
	model				= ServiceAudit
	extra				= 0
	fields				= ['owner', 'entered', 'notes', 'photo', 'audio']
# end ServiceAuditInline

###############################################################
class SpaceAuditInline(admin.TabularInline):
	model				= SpaceAudit
	extra				= 0
	fields				= ['owner', 'entered', 'notes', 'photo', 'audio']
# end SPaceAuditInline
###############################################################
class AccessPointAuditInline(admin.TabularInline):
	model				= AccessPointAudit
	extra				= 0
	fields				= ['owner', 'entered', 'notes', 'photo', 'audio']
# end AccessPointAuditInline

###############################################################
class SessionAdmin(admin.ModelAdmin):
	fields			= ['name', 'start', 'weather']
	list_display	= ['id', 'name', 'start']
	
	search_fields	= ['name']
	#inlines			= [LinkAuditInline, ServiceAuditInline, \
	#				SpaceAuditInline, AccessPointAuditInline]
	#LinkAuditInline.ordering	= ['owner']
	#ServiceAuditInline.ordering	= ['owner']
	#SpaceAuditInline.ordering	= ['owner']
	#AccessPointAuditInline.ordering	= ['owner']
# end sessionAdmin

###############################################################
class FeedbackAdmin(admin.ModelAdmin):
	fields			= ['session', 'entered', 'download_appQ', \
					'why_this_downloadQ', 'not_understand_detail', 'other']
	list_display	= ['id', 'session', 'entered']
		
# end FeedbackAdmin

###############################################################
admin.site.register(ProxySpace, SpaceAdmin)
admin.site.register(Space, SpaceAdmin)
admin.site.register(ProxyLink, LinkAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(ProxyAccessPoint, AccessPointAdmin)
admin.site.register(AccessPoint, AccessPointAdmin)
admin.site.register(ProxyService, ServiceAdmin)
admin.site.register(Service, ServiceAdmin)

admin.site.register(ProxySpaceType, SpaceTypeAdmin)
admin.site.register(ProxyLinkType, LinkTypeAdmin)
admin.site.register(ProxyAccessPointType, AccessPointTypeAdmin)
admin.site.register(ProxyServiceType, ServiceTypeAdmin)

admin.site.register(ProxySpaceStandard, SpaceStandardsAdmin)
admin.site.register(ProxyLinkStandard, LinkStandardsAdmin)
admin.site.register(ProxyAccessPointStandard, AccessPointStandardsAdmin)
admin.site.register(ProxyServiceStandard, ServiceStandardsAdmin)

admin.site.register(ProxySpaceAudit, SpaceAuditAdmin)
admin.site.register(ProxyLinkAudit, LinkAuditAdmin)
admin.site.register(ProxyServiceAudit, ServiceAuditAdmin)
admin.site.register(ProxyAccessPointAudit, AccessPointAuditAdmin)

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(message)
