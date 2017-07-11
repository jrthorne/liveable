##################################################################
FileName		= 'models.py'
# By:			Jason Thorne
# Date:			11-03-2012
# Description: 	The env_issues project
##################################################################
from django.db import models
# r180
import settings
#####################################################################
# Create your models here.
#####################################################################
# r175
class message(models.Model):
	# each message is identified by this.
	identifier				= models.CharField(max_length=80)
	information				= models.TextField()
	def __unicode__(self):
		return self.identifier
	# end unicode
# end message

#####################################################################
# The Foreign key types are defined FIRST in the following 4 objects. 
class SpaceType(models.Model):
	type				= models.CharField(max_length=80)
	def __unicode__(self):
		return self.type
	# end unicode
# end SpaceType
#####################################################################
class LinkType(models.Model):
	type				= models.CharField(max_length=80)
	def __unicode__(self):
		return self.type
	# end unicode
# end LinkType
#####################################################################
class AccessPointType(models.Model):
	type				= models.CharField(max_length=80)
	def __unicode__(self):
		return self.type
	# end unicode
# end AccessPointType
#####################################################################
class ServiceType(models.Model):
	type				= models.CharField(max_length=80)
	def __unicode__(self):
		return self.type
	# end unicode
# end ServiceType

#####################################################################
class SpaceStandards(models.Model):
	reference			= models.CharField(max_length=255)
	element				= models.CharField(max_length=255)
	criteria			= models.CharField(max_length=255)
	comment				= models.TextField(blank=True, null=True)
	type				= models.ForeignKey(SpaceType)
	photo 				= models.ImageField(upload_to='standard', blank=True, null=True)
	def __unicode__(self):
		return self.reference
	# end unicode
# end SpaceStandards
#####################################################################
class LinkStandards(models.Model):
	reference			= models.CharField(max_length=255)
	element				= models.CharField(max_length=255)
	criteria			= models.CharField(max_length=255)
	comment				= models.TextField(blank=True, null=True)
	type				= models.ForeignKey(LinkType)
	photo 				= models.ImageField(upload_to='standard', blank=True, null=True)
	def __unicode__(self):
		return self.reference
	# end unicode
# end LinkStandards
#####################################################################
class ServiceStandards(models.Model):
	reference			= models.CharField(max_length=255)
	element				= models.CharField(max_length=255)
	criteria			= models.CharField(max_length=255)
	comment				= models.TextField(blank=True, null=True)
	type				= models.ForeignKey(ServiceType)
	photo 				= models.ImageField(upload_to='standard', blank=True, null=True)
	def __unicode__(self):
		return self.reference
	# end unicode
# end ServiceStandards
#####################################################################
class AccessPointStandards(models.Model):
	reference			= models.CharField(max_length=255)
	element				= models.CharField(max_length=255)
	criteria			= models.CharField(max_length=255)
	comment				= models.TextField(blank=True, null=True)
	type				= models.ForeignKey(AccessPointType)
	photo 				= models.ImageField(upload_to='standard', blank=True, null=True)
	def __unicode__(self):
		return self.reference
	# end unicode
# end AccessPointStandards

#####################################################################
# the session table lists when audits occur, weather conditions etc
# foreign keys in each of the audit tables link back to session
class Session(models.Model):
	name				= models.CharField(max_length=80)
	start				= models.DateTimeField()
	weather				= models.TextField(blank=True)	
	
	def __unicode__(self):
		return str(self.id) + ':' + self.name
	# end unicode
# end session

#####################################################################
class Space(models.Model):
	latitude			= models.FloatField()
	longitude			= models.FloatField()
	session				= models.ForeignKey(Session)
	entered				= models.DateTimeField(null=True) # allow null for legacy data
	
	# to be replaced by enumerated field in update
	type				= models.ForeignKey(SpaceType)
	address				= models.CharField(max_length=200)
	name				= models.CharField(max_length=80, blank=True, null=True)
	lotId				= models.IntegerField(blank=True, null=True)
	properties			= models.TextField(blank=True, null=True)
	owner				= models.IntegerField(blank=True, null=True)
#	owner				= models.ForeignKey(auth_user)
	# id of space within which this space resides.
	#parent				= models.ForeignKey(Space)
	parent				= models.IntegerField(blank=True, null=True)
	# Set of objects that reside within this space multivalue
	children			= models.IntegerField(blank=True, null=True)
	# set of objects that adjoin this space multivalue
	peers				= models.IntegerField(blank=True, null=True)
	# set of media associated with this space multivalue
	medias				= models.IntegerField(blank=True, null=True)
	# we will get rid of this to be replaced by a media table linking
	# many images for each object.
	photo 				= models.ImageField(upload_to='photo', blank=True, null=True)
	audio				= models.FileField(upload_to='audio', \
							blank=True, null=True)
	score				= models.IntegerField(blank=True, null=True)
	
	def __unicode__(self):
		typeName	= str(self.type)
		return "ID=" + str(self.id) + ":: TYPE=" + typeName + \
		":: ADDDRESS=" + self.address  
	# end unicode
# end Space
#####################################################################
class Link(models.Model):
	latitude			= models.FloatField()
	longitude			= models.FloatField()
	session				= models.ForeignKey(Session)
	entered				= models.DateTimeField(null=True) # allow null for legacy data
	
	# to be replaced by enumerated field in update
	type				= models.ForeignKey(LinkType)
	name				= models.CharField(max_length=80)
	properties			= models.TextField(blank=True, null=True)
	owner				= models.IntegerField(blank=True, null=True)
#	owner				= models.ForeignKey(auth_user)
	# id of space within which this link resides.
	parent				= models.ForeignKey(Space, blank=True, null=True)
	# Set of access points that lie within this link multivalue
	children			= models.IntegerField(blank=True, null=True)
	# set of objects that adjoin this link mutlivalue
	peers				= models.IntegerField(blank=True, null=True)
	# set of media associated with this link multivalue
	medias				= models.IntegerField(blank=True, null=True)
	# we will get rid of this to be replaced by a media table linking
	# many images for each object.
	photo 				= models.ImageField(upload_to='photo', blank=True, null=True)
	audio				= models.FileField(upload_to='audio', \
							blank=True, null=True)
	score				= models.IntegerField(blank=True, null=True)
	
	def __unicode__(self):
		typeName	= str(self.type)
		return "ID=" + str(self.id) + ":: TYPE=" + typeName + \
		":: NAME=" + self.name  
	# end unicode
# end Link
#####################################################################
class AccessPoint(models.Model):
	latitude			= models.FloatField()
	longitude			= models.FloatField()
	session				= models.ForeignKey(Session)
	entered				= models.DateTimeField(null=True) # allow null for legacy data
	
	# to be replaced by enumerated field in update
	type				= models.ForeignKey(AccessPointType)
	name				= models.CharField(max_length=80)
	properties			= models.TextField(blank=True, null=True)
	owner				= models.IntegerField(blank=True, null=True)
#	owner				= models.ForeignKey(auth_user)
	# id of space/link within which this access point resides.
	parentSpace			= models.ForeignKey(Space, blank=True, null=True)
	parentLink			= models.ForeignKey(Link, blank=True, null=True)
	# Set of services that lie within this access point multivalue
	children			= models.IntegerField(blank=True, null=True)
	# set of objects that adjoin this link mutlivalue
	peers				= models.IntegerField(blank=True, null=True)
	# set of media associated with this link multivalue
	medias				= models.IntegerField(blank=True, null=True)
	# we will get rid of this to be replaced by a media table linking
	# many images for each object.
	photo 				= models.ImageField(upload_to='photo', blank=True, null=True)
	audio				= models.FileField(upload_to='audio', \
							blank=True, null=True)
	score				= models.IntegerField(blank=True, null=True)
		
	def __unicode__(self):
		typeName	= str(self.type)
		return "ID=" + str(self.id) + ":: TYPE=" + typeName + \
		":: NAME=" + self.name  
	# end unicode
# end AccessPoint
#####################################################################
class Service(models.Model):
	latitude			= models.FloatField()
	longitude			= models.FloatField()
	session				= models.ForeignKey(Session)
	entered				= models.DateTimeField(null=True) # allow null for legacy data
	
	# to be replaced by enumerated field in update
	type				= models.ForeignKey(ServiceType)
	name				= models.CharField(max_length=80)
	properties			= models.TextField(blank=True, null=True)
	owner				= models.IntegerField(blank=True, null=True)
#	owner				= models.ForeignKey(auth_user)
	# id of space/link within which this access point resides.
	parentSpace			= models.ForeignKey(Space, blank=True, null=True)
	parentLink			= models.ForeignKey(Link, blank=True, null=True)
	parentAP			= models.ForeignKey(AccessPoint, blank=True, null=True)
	# Set of services that lie within this access point multivalue
	children			= models.IntegerField(blank=True, null=True)
	# set of objects that adjoin this link mutlivalue
	peers				= models.IntegerField(blank=True, null=True)
	# set of media associated with this link multivalue
	medias				= models.IntegerField(blank=True, null=True)
	# we will get rid of this to be replaced by a media table linking
	# many images for each object.
	photo 				= models.ImageField(upload_to='photo', blank=True, null=True)
	audio				= models.FileField(upload_to='audio', \
							blank=True, null=True)
	score				= models.IntegerField(blank=True, null=True)
	
	def __unicode__(self):
		typeName	= str(self.type)
		return "ID=" + str(self.id) + ":: TYPE=" + typeName + \
		":: NAME=" + self.name  
	# end unicode
# end Service


#####################################################################
# the people who can participate in the audit session
# (name, gender, age, years resident, comments) 
class Participant(models.Model):
	
	AGEGROUPTYPE		= ( \
		(0, '0-12'), \
		(1, '13-21'), \
		(2, '22-35'), \
		(3, '36-65'), \
		(4, '66-80'), \
		(5, '81+'), \
	)
	email				= models.CharField(max_length=80)
	username			= models.CharField(max_length=80)
	password			= models.CharField(max_length=80, blank=True)
	# r213 Organisation needs to be more tha 80 characters
	organisation		= models.CharField(max_length=255, blank=True)
	dob					= models.DateField(null=True, blank=True) 
	age_group			= models.IntegerField(choices=AGEGROUPTYPE, null=True)
	first_name			= models.CharField(max_length=255, blank=True)
	# r180 moved GENERTYPE to settings
	gender				= models.CharField(max_length=1, choices=settings.GENDERTYPE, blank=True)
	age					= models.IntegerField(null=True, blank=True)
	residentYears		= models.FloatField(blank=True, null=True)
	comment				= models.TextField(blank=True)
	country				= models.CharField(max_length=80, blank=True)
	postcode			= models.CharField(max_length=80, blank=True)
	# many users can be in many sessions R168 removed redundant , through='Participant_Session'
	session				= models.ManyToManyField(Session)
	# r166 
	suburb				= models.CharField(max_length=255, blank=True)
	# r166 was not sure wether to use dob for birth year, but decided to make a new field
	birth_year			= models.IntegerField(null=True, blank=True)
	
	def __unicode__(self):
		return self.email
	# end unicode

# end Participants

#####################################################################
class Participant_Session(models.Model):
	participant			= models.ForeignKey(Participant)
	session				= models.ForeignKey(Session)
# end Participant_Session

#####################################################################
# The audit tables
class SpaceAudit(models.Model):
	session				= models.ForeignKey(Session)
	entered				= models.DateTimeField(null=True,blank=True) # allow null for legacy data
	owner				= models.ForeignKey(Space, blank=True, null=True)
	type				= models.ForeignKey(SpaceType, blank=True, null=True)
	standard			= models.ForeignKey(SpaceStandards, \
						blank=True, null=True)
	# r147 should be conforms to the standard. It was confirms
	conforms			= models.NullBooleanField(blank=True, null=True)
	score				= models.IntegerField(blank=True, null=True)
	notes				= models.TextField(blank=True, null=True)
	photo 				= models.ImageField(upload_to='photo', \
							blank=True, null=True)
	audio				= models.FileField(upload_to='audio', \
							blank=True, null=True)
	def __unicaode__(self):
		return self.notes[0:20] # first 20 chars of the notes
	# end unicode
# end SpaceAudit
#####################################################################
class LinkAudit(models.Model):
	session				= models.ForeignKey(Session)
	entered				= models.DateTimeField(null=True, blank=True) # allow null for legacy data
	owner				= models.ForeignKey(Link, blank=True, null=True)
	type				= models.ForeignKey(LinkType, blank=True, null=True)
	standard			= models.ForeignKey(LinkStandards, \
						blank=True, null=True)
	# r147 should be conforms to the standard. It was confirms
	conforms			= models.NullBooleanField(blank=True, null=True)
	score				= models.IntegerField(blank=True, null=True)
	notes				= models.TextField(blank=True, null=True)
	photo 				= models.ImageField(upload_to='photo', \
							blank=True, null=True)
	audio				= models.FileField(upload_to='audio', \
							blank=True, null=True)
	def __unicaode__(self):
		return self.notes[0:20] # first 20 chars of the notes
	# end unicode
# end LinkAudit
#####################################################################
class ServiceAudit(models.Model):
	session				= models.ForeignKey(Session)
	entered				= models.DateTimeField(null=True, blank=True) # allow null for legacy data
	owner				= models.ForeignKey(Service, blank=True, null=True)
	type				= models.ForeignKey(ServiceType, blank=True, null=True)
	standard			= models.ForeignKey(ServiceStandards, \
						blank=True, null=True)
	# r147 should be conforms to the standard. It was confirms
	conforms			= models.NullBooleanField(blank=True, null=True)
	score				= models.IntegerField(blank=True, null=True)
	notes				= models.TextField(blank=True, null=True)
	photo 				= models.ImageField(upload_to='photo', \
							blank=True, null=True)
	audio				= models.FileField(upload_to='audio', \
							blank=True, null=True)
	def __unicaode__(self):
		return self.notes[0:20] # first 20 chars of the notes
	# end unicode
# end ServiceAudit
#####################################################################
class AccessPointAudit(models.Model):
	session				= models.ForeignKey(Session)
	entered				= models.DateTimeField(null=True, blank=True) # allow null for legacy data
	owner				= models.ForeignKey(AccessPoint, blank=True, null=True)
	type				= models.ForeignKey(AccessPointType, \
						blank=True, null=True)
	standard			= models.ForeignKey(AccessPointStandards, \
						blank=True, null=True)
	# r147 should be conforms to the standard. It was confirms
	conforms			= models.NullBooleanField(blank=True, null=True)
	score				= models.IntegerField(blank=True, null=True)
	notes				= models.TextField(blank=True, null=True)
	photo 				= models.ImageField(upload_to='photo', \
							blank=True, null=True)
	audio				= models.FileField(upload_to='audio', \
							blank=True, null=True)
	def __unicaode__(self):
		return self.notes[0:20] # first 20 chars of the notes
	# end unicode
# end AccessPointAudit
#####################################################################
# r131 added recording of liveability application problems
class Feedback(models.Model):
	APPDOWNLOADCHOICES		= ( \
		(0, 'iPad'), \
		(1, 'iPhone'), \
		(2, 'Both'), \
		(3, 'Neither'), \
	)
	
	session				= models.ForeignKey(Session, null=True, blank=True) # null for anonymus
	# allow null for legacy data, but not blank, so date has to be filled in the form
	entered				= models.DateTimeField(null=True) 
	# r153
	download_appQ		= models.IntegerField(choices=APPDOWNLOADCHOICES)
	why_this_downloadQ	= models.TextField(blank=True)
	not_understand_detail = models.TextField(blank=True)
	other				= models.TextField(blank=True)
	
	def __unicaode__(self):
		return self.details[0:20] # first 20 chars of the notes
	# end unicode
# end Feedback

#####################################################################
class ProxySpace(Space):
	class Meta:
		proxy			= True
		# If you're define ProxySpace inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Object'
		
		# set following lines to display ProxySpace as Space
		verbose_name 			= Space._meta.verbose_name
		verbose_name_plural		= Space._meta.verbose_name_plural
	# end class meta
# end class ProxySpace

#####################################################################
class ProxySpaceAudit(SpaceAudit):
	class Meta:
		proxy			= True
		# If you're define ProxySpace inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Audit'
		
		# set following lines to display ProxySpace as Space
		verbose_name 			= SpaceAudit._meta.verbose_name
		verbose_name_plural		= SpaceAudit._meta.verbose_name_plural
	# end class meta
# end class ProxySpace

#####################################################################
class ProxySpaceStandard(SpaceStandards):
	class Meta:
		proxy			= True
		# If you're define ProxySpace inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Standard'
		
		# set following lines to display ProxySpace as Space
		verbose_name 			= SpaceStandards._meta.verbose_name
		verbose_name_plural		= "Space Standards"
	# end class meta
# end class ProxySpace

#####################################################################
class ProxySpaceType(SpaceType):
	class Meta:
		proxy			= True
		# If you're define ProxySpace inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Type'
		
		# set following lines to display ProxySpace as Space
		verbose_name 			= SpaceType._meta.verbose_name
		verbose_name_plural		= SpaceType._meta.verbose_name_plural
	# end class meta
# end class ProxySpace

#####################################################################
class ProxyLink(Link):
	class Meta:
		proxy			= True
		# If you're define ProxyLink inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Object'
		
		# set following lines to display ProxyLink as Link
		verbose_name 			= Link._meta.verbose_name
		verbose_name_plural		= Link._meta.verbose_name_plural
	# end class meta
# end class ProxyLink

#####################################################################
class ProxyLinkAudit(LinkAudit):
	class Meta:
		proxy			= True
		# If you're define ProxyLink inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Audit'
		
		# set following lines to display ProxyLink as Link
		verbose_name 			= LinkAudit._meta.verbose_name
		verbose_name_plural		= LinkAudit._meta.verbose_name_plural
	# end class meta
# end class ProxyLink

#####################################################################
class ProxyLinkStandard(LinkStandards):
	class Meta:
		proxy			= True
		# If you're define ProxyLink inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Standard'
		
		# set following lines to display ProxyLink as Link
		verbose_name 			= LinkStandards._meta.verbose_name
		verbose_name_plural		= "Link Standards"
	# end class meta
# end class ProxyLink

#####################################################################
class ProxyLinkType(LinkType):
	class Meta:
		proxy			= True
		# If you're define ProxyLink inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Type'
		
		# set following lines to display ProxyLink as Link
		verbose_name 			= LinkType._meta.verbose_name
		verbose_name_plural		= LinkType._meta.verbose_name_plural
	# end class meta
# end class ProxyLink

#####################################################################
class ProxyAccessPoint(AccessPoint):
	class Meta:
		proxy			= True
		# If you're define ProxyAccessPoint inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Object'
		
		# set following lines to display ProxyAccessPoint as AccessPoint
		verbose_name 			= AccessPoint._meta.verbose_name
		verbose_name_plural		= AccessPoint._meta.verbose_name_plural
	# end class meta
# end class ProxyAccessPoint

#####################################################################
class ProxyAccessPointAudit(AccessPointAudit):
	class Meta:
		proxy			= True
		# If you're define ProxyAccessPoint inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Audit'
		
		# set following lines to display ProxyAccessPoint as AccessPoint
		verbose_name 			= AccessPointAudit._meta.verbose_name
		verbose_name_plural		= AccessPointAudit._meta.verbose_name_plural
	# end class meta
# end class ProxyAccessPoint

#####################################################################
class ProxyAccessPointStandard(AccessPointStandards):
	class Meta:
		proxy			= True
		# If you're define ProxyAccessPoint inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Standard'
		
		# set following lines to display ProxyAccessPoint as AccessPoint
		verbose_name 			= AccessPointStandards._meta.verbose_name
		verbose_name_plural		= "Access Point Standards"
	# end class meta
# end class ProxyAccessPoint

#####################################################################
class ProxyAccessPointType(AccessPointType):
	class Meta:
		proxy			= True
		# If you're define ProxyAccessPoint inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Type'
		
		# set following lines to display ProxyAccessPoint as AccessPoint
		verbose_name 			= AccessPointType._meta.verbose_name
		verbose_name_plural		= AccessPointType._meta.verbose_name_plural
	# end class meta
# end class ProxyAccessPoint

#####################################################################
class ProxyService(Service):
	class Meta:
		proxy			= True
		# If you're define ProxyService inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Object'
		
		# set following lines to display ProxyService as Service
		verbose_name 			= Service._meta.verbose_name
		verbose_name_plural		= Service._meta.verbose_name_plural
	# end class meta
# end class ProxyService

#####################################################################
class ProxyServiceAudit(ServiceAudit):
	class Meta:
		proxy			= True
		# If you're define ProxyService inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Audit'
		
		# set following lines to display ProxyService as Service
		verbose_name 			= ServiceAudit._meta.verbose_name
		verbose_name_plural		= ServiceAudit._meta.verbose_name_plural
	# end class meta
# end class ProxyService

#####################################################################
class ProxyServiceStandard(ServiceStandards):
	class Meta:
		proxy			= True
		# If you're define ProxyService inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Standard'
		
		# set following lines to display ProxyService as Service
		verbose_name 			= ServiceStandards._meta.verbose_name
		verbose_name_plural		= "Service Standards"
	# end class meta
# end class ProxyService

#####################################################################
class ProxyServiceType(ServiceType):
	class Meta:
		proxy			= True
		# If you're define ProxyService inside env_issues/models.py
		# its app_label is set to "env_issues" automatically
		# or else comment out following line to specify it explicity
		app_label		= 'Type'
		
		# set following lines to display ProxyService as Service
		verbose_name 			= ServiceType._meta.verbose_name
		verbose_name_plural		= ServiceType._meta.verbose_name_plural
	# end class meta
# end class ProxyService

#####################################################################


