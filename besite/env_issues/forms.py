##################################################################
FileName		= 'forms.py'
# By:			Jason Thorne
# Date:			11-03-2012
# Description: 	The env_issues project
##################################################################
from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, CheckboxInput
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe

from env_issues.models import Participant, Session, Participant_Session, Feedback,\
SpaceAudit, LinkAudit, AccessPointAudit, ServiceAudit, Space, Link, AccessPoint, Service
import settings
import datetime

# r190
###############################################################
class spaceAuditForm(forms.ModelForm):
	class Meta:
		model			= SpaceAudit
		fields			= ['entered', 'owner', 'score', 'notes', 'photo', 'audio']
	# end Meta
	
	notes				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'10', 'cols':'80'}), required=False)
	
	# make the datetime entered read only
	entered				= forms.DateTimeField(required=False,\
    		widget=forms.DateTimeInput(attrs={'readonly':'readonly'}))
	
# end spaceAuditForm

###############################################################
class linkAuditForm(forms.ModelForm):
	class Meta:
		model			= LinkAudit
		fields			= ['entered', 'owner', 'score', 'notes', 'photo', 'audio']
	# end Meta
	
	notes				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'10', 'cols':'80'}), required=False)
	
	# make the datetime entered read only
	entered				= forms.DateTimeField(required=False, \
    		widget=forms.DateTimeInput(attrs={'readonly':'readonly'}))
	
# end linkAuditForm

###############################################################
class accessPointAuditForm(forms.ModelForm):
	class Meta:
		model			= AccessPointAudit
		fields			= ['entered', 'owner', 'score', 'notes', 'photo', 'audio']
	# end Meta
	
	notes				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'10', 'cols':'80'}), required=False)
		
	# make the datetime entered read only
	entered				= forms.DateTimeField(required=False, \
    		widget=forms.DateTimeInput(attrs={'readonly':'readonly'}))
	
# end accessPointAuditForm

###############################################################
class serviceAuditForm(forms.ModelForm):
	class Meta:
		model			= ServiceAudit
		fields			= ['entered', 'owner', 'score', 'notes', 'photo', 'audio']
	# end Meta
	
	notes				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'10', 'cols':'80'}), required=False)
		
	# make the datetime entered read only
	entered				= forms.DateTimeField(required=False, \
    		widget=forms.DateTimeInput(attrs={'readonly':'readonly'}))
	
# end serviceAuditForm

# r197
###############################################################
class spaceForm(forms.ModelForm):
	class Meta:
		model			= Space
		fields			= ['entered', 'type', 'address', 'name', 'properties', 'photo', 'audio']
	# end Meta
	
	address				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'1', 'cols':'80'}), max_length=40, required=False)
	properties			= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'10', 'cols':'80'}), max_length=40, required=False)
	name				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'1', 'cols':'80'}), max_length=40, required=False)
		
	# make the datetime entered read only
	entered				= forms.DateTimeField(required=False,\
    		widget=forms.DateTimeInput(attrs={'readonly':'readonly'}))
	
# end spaceForm

###############################################################
class linkForm(forms.ModelForm):
	class Meta:
		model			= Link
		fields			= ['entered', 'type', 'name', 'properties', 'photo', 'audio']
	# end Meta
	
	properties			= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'10', 'cols':'80'}), max_length=40, required=False)
	name				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'1', 'cols':'80'}), max_length=40, required=False)
	
	# make the datetime entered read only
	entered				= forms.DateTimeField(required=False, \
    		widget=forms.DateTimeInput(attrs={'readonly':'readonly'}))
	
# end linkForm

###############################################################
class accessPointForm(forms.ModelForm):
	class Meta:
		model			= AccessPoint
		fields			= ['entered', 'type', 'name', 'properties', 'photo', 'audio']
	# end Meta
	
	properties			= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'10', 'cols':'80'}), max_length=40, required=False)
	name				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'1', 'cols':'80'}), max_length=40, required=False)
		
	# make the datetime entered read only
	entered				= forms.DateTimeField(required=False, \
    		widget=forms.DateTimeInput(attrs={'readonly':'readonly'}))
	
# end accessPointForm

###############################################################
class serviceForm(forms.ModelForm):
	class Meta:
		model			= Service
		fields			= ['entered', 'type', 'name', 'properties', 'photo', 'audio']
	# end Meta
	
	properties			= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'10', 'cols':'80'}), max_length=40, required=False)
	name				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'1', 'cols':'80'}), max_length=40, required=False)
		
	# make the datetime entered read only
	entered				= forms.DateTimeField(required=False, \
    		widget=forms.DateTimeInput(attrs={'readonly':'readonly'}))
	
# end serviceForm

###############################################################
class loginForm(forms.Form):
	session		= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'1', 'cols':'50'}), max_length=80, required=True,
		help_text="Enter your email address or the session name")
		
	
	def clean_session(self):
		# need to make sure that the session exists or is null
		sessionName		= self.cleaned_data.get('session', None)
		# r189 remove tabs newlines etc
		sessionName		= sessionName.replace("\n", '')
		sessionName		= sessionName.replace("\r", '')
		sessionName		= sessionName.replace("\t", '')
		
		# make it a session instance with this name or flag an error
		try:
			mySession		= Session.objects.get(name=sessionName)
		except ObjectDoesNotExist:
			msg			= mark_safe("Session named<BR>'%s'<BR>does not exist." %sessionName)
			raise forms.ValidationError(msg)
		else:
			return sessionName
		# end try
	# end clean_session
# end loginForm

###############################################################
class feedbackForm(forms.ModelForm):
	APPDOWNLOADCHOICES		= ( \
		(0, 'iPad'), \
		(1, 'iPhone'), \
		(2, 'Both'), \
		(3, 'Neither'), \
	)
	
	# r169
	class Meta:
		model 			= Feedback
		fields			= ['session_name', 'download_appQ', 'why_this_downloadQ', \
						'not_understand_detail', 'other']
	# end Meta

	session_name		= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'1', 'cols':'50'}), max_length=80, required=False,
		help_text="Enter your email address (or the session name) you used when you registered"+\
					" the application, or leave blank for anonymous", label="Email address")
		
	download_appQ		= forms.ChoiceField(choices=APPDOWNLOADCHOICES, \
	label='Download application?', \
	help_text="Which platform did you use?", required=True)
	why_this_downloadQ	= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'5', 'cols':'100'}),required=False, \
		label="Why?", help_text="Why did you choose this platform? What version of the software did you use?")
	not_understand_detail = forms.CharField(label="Difficulties", \
		widget=forms.Textarea(\
		attrs={'rows':'5', 'cols':'100'}), required=False, \
		help_text="Things that were not clear or made the application difficult to use")

	other				= forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'5', 'cols':'100'}), required=False,
		help_text="Any other advice/comments you would like to leave")
		
	######## convert the session instance into 
	def clean_session_name(self):
		# need to make sure that the session exists or is null
		sessionName		= self.cleaned_data.get('session_name', None)
		print sessionName
		# make it a session instance with this name or flag an error
		try:
			mySession		= Session.objects.get(name=sessionName)
		except ObjectDoesNotExist:
			if sessionName == "": # the feedback is anonlymus for session Name blank
				return self.cleaned_data['session_name']
			else:
				msg			= "Session named '%s' does not exist." %sessionName
				msg			+= " Enter blank for an annonymous feedback."
				raise forms.ValidationError(msg)
			# end if
		else:
			return self.cleaned_data['session_name']
		# end try
	# end clean_session
		
# end feedbackForm

###############################################################
# r213 - This is originally for the application registration form
# but may also be used for a web based form
# I use ModelForm or Meta, but I have already written the view to create
# the participant and session records. However, the way I did it was not good.
# next time, any form wether HTML or as in this case, HTTP via mobile application
# should be done via the same django form handling
#### NOTE: To maintiain compatibility with V1 of the app, I can only make email
# compulsory in the application handing view.
class registerForm(forms.ModelForm):

	class Meta:
		model			= Participant
		fields			= ['email', 'first_name', 'gender', 'birth_year', 'organisation', \
						'suburb', 'residentYears']
	# end Meta
	
	# The compulsory fields
	email				= forms.EmailField(widget=forms.Textarea(\
		attrs={'rows':'1', 'cols':'50'}), max_length=80, required=True,
		help_text="Enter your email address", label="Email")
	first_name			= forms.CharField(max_length=255, required=True, label="First Name")
	# need a clean field here as only text returned
	gender 				= forms.ChoiceField(choices=settings.GENDERTYPE, required=True,\
		label="Gender")
	birth_year 			= forms.IntegerField(required=True, label="Year of Birth")
	
	# The non compulsory fields
	organisation 		= forms.CharField(max_length=255, required=False, label="Organisation")
	suburb				= forms.CharField(max_length=255, required=False, label="Suburb")
	residentYears		= forms.FloatField(required=False, label="Years Resident")
	
	# needs to be between 13-100 years old
	def clean_birth_year(self):
		thisYear = datetime.datetime.now().year
		myBirthYear		= self.cleaned_data.get('birth_year', None)
		
		# must be of minimum age
		if myBirthYear > (thisYear - settings.MINIMUM_AGE):
			msg			= mark_safe("You must be at least<BR>%d years old." %settings.MINIMUM_AGE)
			raise forms.ValidationError(msg)
		elif myBirthYear < (thisYear - 120): # cant be over 120 years old
			msg			= mark_safe("Invalid year, this makes<BR>you %d years old." %(thisYear-myBirthYear))
			raise forms.ValidationError(msg)
		else:
			return myBirthYear
		# end if
	# end clean_birth_year
	
# end registerForm


####################
class registerFormWeb(forms.ModelForm):

	class Meta:
		model			= Participant
		fields			= ['email', 'first_name', 'gender', 'birth_year', 'organisation', \
						'suburb', 'residentYears']
	# end Meta
	
	# The compulsory fields
	email				= forms.EmailField(widget=forms.Textarea(\
		attrs={'rows':'1', 'cols':'50'}), max_length=80, required=True,
		help_text="Enter your email address", label="Email")
	first_name			= forms.CharField(max_length=255, required=True, label="First Name")
	# need a clean field here as only text returned
	gender 				= forms.ChoiceField(choices=settings.GENDERTYPE, required=True,\
		label="Gender")
	birth_year 			= forms.IntegerField(required=True, label="Year of Birth")
	
	# The non compulsory fields
	organisation 		= forms.CharField(max_length=255, required=False, label="Organisation")
	suburb				= forms.CharField(max_length=255, required=False, label="Suburb")
	residentYears		= forms.FloatField(required=False, label="Years Resident")
	
	# Terms Of Service
	tos 				= forms.BooleanField(widget=forms.CheckboxInput,
						error_messages={'required': _("You must agree to the terms to register")},
						label='I agree to the <a href="/getMessage/disclaimer_register/">terms &amp; conditions</a>')
	
	# needs to be between 13-100 years old
	def clean_birth_year(self):
		thisYear = datetime.datetime.now().year
		myBirthYear		= self.cleaned_data.get('birth_year', None)
		
		# must be of minimum age
		if myBirthYear > (thisYear - settings.MINIMUM_AGE):
			msg			= mark_safe("You must be at least<BR>%d years old." %settings.MINIMUM_AGE)
			raise forms.ValidationError(msg)
		elif myBirthYear < (thisYear - 120): # cant be over 120 years old
			msg			= mark_safe("Invalid year, this makes<BR>you %d years old." %(thisYear-myBirthYear))
			raise forms.ValidationError(msg)
		else:
			return myBirthYear
		# end if
	# end clean_birth_year
	
# end registerForm