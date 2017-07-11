##################################################################
FileName		= 'views.py'
# By:			Jason Thorne
# Date:			11-03-2012
# Description: 	The env_issues project
##################################################################
import json
import datetime, time
import string # r131 for use in filtering non printing characers
import os
import tempfile

import JRTreportlabHTML as jrtH
import JRTreportlabCharts as jrtC

from django.conf import settings
from env_issues.models import Participant, Session, Participant_Session, Feedback, \
Space, Link, AccessPoint, Service, SpaceType, LinkType, AccessPointType, ServiceType, \
message, SpaceAudit, LinkAudit, ServiceAudit, AccessPointAudit

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from env_issues.forms import *
from django.template import RequestContext
from math import sin, cos, pi, acos
from django.forms.models import model_to_dict
from django.core.mail import send_mail

"""
Used for converting Warringa data
import pyproj as pyp
import shapefile
import numpy as np
from dbfpy import dbf
"""

statusKey			= 'status'

# r130 I did not end up using this. 
class staticVars:
	navigation		= ""
# end class

#################################################################
# def convWar(request):
# # open the database file.....
# 	myDir	= '/www/built/UNSW_2013/'
# 	db 		= dbf.Dbf(myDir + "PD0217_st_furniture.dbf", readOnly=1)
# 	# whose records line up with the shape file
# 	sf = shapefile.Reader(myDir + "PD0217_st_furniture")
# 	shapeRecs	= sf.shapeRecords()
# 	
# 	# for conversion to latitude and longitude
# 	UTMstring		= "+proj=tmerc +lat_0=0.0 +lon_0=153.0 +k=0.9996 +x_0=500000.0 "
# 	UTMstring		+= "+y_0=10000000.0"
# 	UTM2latlong 	= pyp.Proj(UTMstring)
# 	
# 	warringahSession	= Session.objects.get(name="warringah")
# 	
# 	#for i in range(min(10,len(db))):
# 	for i in range(len(db)):
# 		rec = db[i]
# 		servName	= ""
# 		servProps	= ""
# 		for fldName in db.fieldNames:
# 			print '%s:\t %s' %(fldName, rec[fldName])
# 
# 			if fldName[:10] == "DESCRIPTIO":
# 				# find out if the type has been seen before
# 				thisType	= rec[fldName]
# 				
# 				# see if we have a type in the database
# 				try:
# 					type4import = ServiceType.objects.get(type=thisType)
# 				except ServiceType.DoesNotExist:
# 					type4import = ServiceType(type=thisType)
# 					type4import.save()
# 				# end try
# 				
# 				servName 		+= thisType + ", "
# 			# end if
# 			
# 			# if this field is the name of the record, then store it
# 			if fldName[:9] == "SECT_FROM":
# 				servName 		+= rec[fldName]
# 			# end if
# 			
# 			servProps			+= str(rec[fldName]) + "\n"
# 			
# 		# next fldName
# 		
# 		# now get the latitude and longitude for this asset
# 		UTMcoord	= shapeRecs[i].shape.points[0]
# 		North		= UTMcoord[1]
# 		East		= UTMcoord[0]
# 		longLat		= UTM2latlong(East, North, inverse=True)
# 		# reverse for cut and paste to google maps
# 		latLong		= (longLat[1], longLat[0])
# 		
# 		print servProps
# 		print "Latitude, Longitude for %s" %servName
# 		print latLong
# 		print
# 		print "*********************************************************************"
# 		
# 		rightNow			= datetime.datetime.now()
# 		
# 		# create a new service record
# 		newSvc		= Service(name=servName, session=warringahSession, type=type4import, \
# 					properties=servProps, latitude=longLat[1], longitude=longLat[0], \
# 					entered=rightNow)
# 		newSvc.save()
# 	# next i
# 	
# 	db.close()
# 	
# 	myResponse = "<h1>Finished at %s importing %d records</h1>" %(str(rightNow), len(db))
# 	return HttpResponse(myResponse)
# # end convWar

#################################################################
# r190
def editAudit(request, auditType, auditID):
	if auditType=="space":
		theAudit	= get_object_or_404(SpaceAudit, pk=auditID)
		form 		= spaceAuditForm(request.POST, instance=theAudit)
	elif auditType=="link":
		theAudit	= get_object_or_404(LinkAudit, pk=auditID)
		form 		= linkAuditForm(request.POST, instance=theAudit)
	elif auditType=="accesspoint":
		theAudit	= get_object_or_404(AccessPointAudit, pk=auditID)
		form 		= accessPointAuditForm(request.POST, instance=theAudit)
	elif auditType=="service":
		theAudit	= get_object_or_404(ServiceAudit, pk=auditID)
		form 		= serviceAuditForm(request.POST, instance=theAudit)
	# end if - NOTE should have default 404 here.
	
	theSession		= theAudit.session
	
	if request.method == 'POST':
		
		if form.is_valid():
			form.save()
			# return to the session report
			return HttpResponseRedirect('/built/%s/' %theAudit.session.id)
		# end if
	else:
		if auditType=="space":
			form 		= spaceAuditForm(instance=theAudit)
		elif auditType=="link":
			form 		= linkAuditForm(instance=theAudit)
		elif auditType=="accesspoint":
			form 		= accessPointAuditForm(instance=theAudit)
		elif auditType=="service":
			form 		= serviceAuditForm(instance=theAudit)
		# end if - NOTE should have default 404 here.
	# endif
	
	
	return render_to_response('env_issues/audit_form.html', locals(), \
		context_instance=RequestContext(request))
# end editAudit

#################################################################
# r197 
def editObject(request, objectType, objectID):
	if objectType=="space":
		theObject	= get_object_or_404(Space, pk=objectID)
		form 		= spaceForm(request.POST, instance=theObject)
	elif objectType=="link":
		theObject	= get_object_or_404(Link, pk=objectID)
		form 		= linkForm(request.POST, instance=theObject)
	elif objectType=="accesspoint":
		theObject	= get_object_or_404(AccessPoint, pk=objectID)
		form 		= accessPointForm(request.POST, instance=theObject)
	elif objectType=="service":
		theObject	= get_object_or_404(Service, pk=objectID)
		form 		= serviceForm(request.POST, instance=theObject)
	# end if - NOTE should have default 404 here.
	
	theSession		= theObject.session
	
	if request.method == 'POST':
		
		if form.is_valid():
			form.save()
			# return to the session report
			return HttpResponseRedirect('/built/%s/' %theObject.session.id)
		# end if
	else:
		if objectType =="space":
			form 		= spaceForm(instance=theObject)
		elif objectType =="link":
			form 		= linkForm(instance=theObject)
		elif objectType =="accesspoint":
			form 		= accessPointForm(instance=theObject)
		elif objectType =="service":
			form 		= serviceForm(instance=theObject)
		# end if - NOTE should have default 404 here.
	# endif
	
	
	return render_to_response('env_issues/object_form.html', locals(), \
		context_instance=RequestContext(request))
# end editAudit

###########################################################
# r197
def objectListReport(request, sessionId):
	# get the associated session first. 
	mySession		= Session.objects.get(pk=sessionId)


	
	return render_to_response('env_issues/objects.html', locals())	
	"""	DetailView.as_view(
				model=Session,
				template_name='env_issues/audits.html')"""
	
# end objectListReport

#########################################
# r197 login get the session name, translate to the ID and then redirect 
# to the object list page
def loginObject(request):	
	# used by form
	whereNext			= 'List Objects'
	
	usernameKey				= 'session'

	# If we submitted the form
	if request.method == 'POST':
		# get the posted data
		form		= loginForm(request.POST)
		if form.is_valid():
			cd		= form.cleaned_data

			# get the session
			mySession		= Session.objects.get(name=cd[usernameKey])
			# r130 Log in function is multi use depending on where it was 
			# called from
			return HttpResponseRedirect('/built/objectMap/%d/' %mySession.id)
			
		# end if
		
	else:
		# If we didn't post, send the test cookie along with the login form
		request.session.set_test_cookie()
		form				= loginForm()
	# end if
	
	return render_to_response('env_issues/login_form.html', locals(), \
			context_instance=RequestContext(request))
# end login
			
#########################################
# login get the session name, translate to the ID and then redirect 
# either to the map or with update r130 to the log problem page
def login(request):	
	
	usernameKey				= 'session'
	# r130 the only issue is that these strings need to be updated independently 
	# in the livability site
	tokenMap				= 'loginMap'
	tokenLogprob			= 'loginFB'
	
	if tokenLogprob in request.path_info:
		redirectTo			= 'feedback'
		whereNext			= 'Give feedback'
	else: # default
		redirectTo			= 'map'
		whereNext			= 'Show audits'
	# end if

	# If we submitted the form
	if request.method == 'POST':
		# get the posted data
		form		= loginForm(request.POST)
		if form.is_valid():
			cd		= form.cleaned_data

			# get the session
			mySession		= Session.objects.get(name=cd[usernameKey])
			# r130 Log in function is multi use depending on where it was 
			# called from
			return HttpResponseRedirect('/built/%s/%d/' %(redirectTo, mySession.id))
			
		# end if
		
	else:
		# If we didn't post, send the test cookie along with the login form
		request.session.set_test_cookie()
		form				= loginForm()
	# end if
	
	return render_to_response('env_issues/login_form.html', locals(), \
			context_instance=RequestContext(request))
# end login

#################################################################
# this is done more DRY in r130
def feedback(request):
	# r169 dont get the session first. It is not passed. People can leave anonymous feedback
	
	rightNow			= datetime.datetime.now()
	myFeedback			= Feedback(entered=rightNow)
	
	# if we submited the form
	if request.method == 'POST':
		form			= feedbackForm(request.POST, instance=myFeedback)
		if form.is_valid():
			cd			= form.cleaned_data 
			# get the session name, and convert it to a session. It would have
			# been checked in the form as to validity
			mySessNm	= cd['session_name']
			if mySessNm:
				mySession		= Session.objects.get(name=mySessNm)
				fb				= form.save(commit=False)
				fb.session		= mySession
				fb.save()
			else:
				form.save()
			# end if
			
			# tell the user it has been submitted thanks
			myResponse = "Your feedback has been submitted successfully<BR>"
			myResponse += "<a href='http://www.liveable.eng.unsw.edu.au'>Return</a>"
			return HttpResponse(myResponse)
		# end if
	else:
		form			= feedbackForm(instance=myFeedback)
	# end if
	
	return render_to_response('env_issues/feedback_form.html', locals(), \
			context_instance=RequestContext(request))
	
# end feedback

######################################################
# This generates the PDF of the audits made for a particular session. 
# The audits exist in four tables, and all of them are collected in a 
# list of strings so the figure can be produced first on the PDF, followed
# by a list of audits.
def auditListReportPDF(request, sessionId):
	# get the associated session first. 
	mySession		= Session.objects.get(pk=sessionId)

	# prepare data for the report
	# SPACE
	auditList		= mySession.spaceaudit_set.all()
	
	spaceAuditCnt	= len(auditList) 
	if spaceAuditCnt > 0:
		spaceAudits		= "<br /><ul>"
		
		# remove the blank lines in notes, as it stuffs up the renering of points on the map
		for i in auditList:
			if i.notes == None: 
				i.notes = ""
				i.save()
			# end if
			i.notes		= i.notes.replace("\n", '')
			i.notes		= i.notes.replace("\r", '')
			i.notes		= i.notes.replace("\t", '')
			mapLat		= i.owner.latitude
			mapLong		= i.owner.longitude
			spaceAudits	+= "<li>" + i.notes + "</li>"  
		# next i
		
		spaceAudits		+= "</ul><br />"
	else:
		spaceAudits		= None
	# end if
	
	# SERVICE
	auditList			= mySession.serviceaudit_set.all()
	serviceAuditCnt		= len(auditList)
	if serviceAuditCnt > 0:
		serviceAudits	= "<br /><ul>"
		
		# remove the blank lines in notes, as it stuffs up the rendering
		for i in auditList:
			if i.notes == None: 
				i.notes = ""
				i.save()
			# end if
			i.notes		= i.notes.replace("\n", '')
			i.notes		= i.notes.replace("\r", '')
			i.notes		= i.notes.replace("\t", '')
			mapLat		= i.owner.latitude
			mapLong		= i.owner.longitude
			serviceAudits	+= "<li>" + i.notes + "</li>"  
		# next i
		
		serviceAudits	+= "</ul><br />"
	else:
		serviceAudits	= None
	# end if

	# LINK
	auditList			= mySession.linkaudit_set.all()
	linkAuditCnt		= len(auditList)
	if linkAuditCnt > 0:
		linkAudits		= "<br /><ul>"
		
		# remove the blank lines in notes, as it stuffs up the renering of points on the map
		for i in auditList:
			if i.notes == None: 
				i.notes = ""
				i.save()
			# end if
			i.notes		= i.notes.replace("\n", '')
			i.notes		= i.notes.replace("\r", '')
			i.notes		= i.notes.replace("\t", '')
			mapLat		= i.owner.latitude
			mapLong		= i.owner.longitude
			linkAudits	+= "<li>" + i.notes + "</li>"  
		# next i
		
		linkAudits		+= "</ul><br />"
	else:
		linkAudits		= None
	# end if
	
	# ACCESS POINT
	auditList	= mySession.accesspointaudit_set.all()
	accessPointAuditCnt		= len(auditList)
	if accessPointAuditCnt > 0:
		accessPointAudits	= "<br /><ul>"
		
		# remove the blank lines in notes, as it stuffs up the renering of points on the map
		for i in auditList:
			if i.notes == None: 
				i.notes = ""
				i.save()
			# end if
			i.notes		= i.notes.replace("\n", '')
			i.notes		= i.notes.replace("\r", '')
			i.notes		= i.notes.replace("\t", '')
			mapLat		= i.owner.latitude
			mapLong		= i.owner.longitude
			accessPointAudits	+= "<li>" + i.notes + "</li>"  
		# next i
		
		accessPointAudits	+= "</ul><br />"
	else:
		accessPointAudits	= None
	# end if
	
	# create an instance of the report
	file = tempfile.NamedTemporaryFile()
	e = jrtH.PdfA4Letter(file.name)
	
	# write a heading for the report
	e.h1(mySession.name)
	e.text(mySession.weather + " on " + str(mySession.start) + "<br /><br />")
	
	sumAudits				= spaceAuditCnt + serviceAuditCnt + linkAuditCnt + accessPointAuditCnt
	# If there are audits, then report on them, otherwise report that there 
	# were none for this session
	if sumAudits:
		# the drawing has been saved as jpg in the html view function, 
		imgAnalysisPie						= "analysisPie"
		# debugging is on my machine. In settings MEDIA_ROOT is set to static if on
		# my machine, but I could not set MEDIA_URL to STATIC_URL, as DJANGO does not
		# like this.
		if settings.PDFDEBUG:
			media_url						= settings.STATIC_URL
			media_root						= settings.STATICFILES_DIRS[0]
		else:
			media_url						= settings.MEDIA_URL
			media_root						= settings.MEDIA_ROOT
		# end if
		
		ref = media_root + "images/" + imgAnalysisPie + '.jpg' 
		e.image(ref, width=jrtH.frame_width, height=10*jrtH.cm)
		
		if spaceAudits:
			e.h2(u'Space Audits')
			e.text(spaceAudits)
		# end if
		if serviceAudits:
			e.h2(u'Service Audits')
			e.text(serviceAudits)
		# end if
		if linkAudits:
			e.h2(u'Link Audits')
			e.text(linkAudits)
		# end if
		if accessPointAudits:
			e.h2(u'Access Point Audits')
			e.text(accessPointAudits)
		# end if
		
	else:
		e.text(u'There were no audits for this session')
	# end if
	
	e.build()

	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=gugus.pdf'
	response.write(file.read()) 
	file.close()
	return response	
	
	
# end auditListReportPDF

#################################################################
# this is a quick fix function. the template does all the work except create 
# the pie chart. This way of doing things is not DRY. I am repeating myself, 
# because the template was already written.
def auditListReport(request, sessionId):
	# get the associated session first. 
	mySession		= Session.objects.get(pk=sessionId)

	# prepare data for the report
	# SPACE
	spaceAuditList		= mySession.spaceaudit_set.all()
	
	spaceAuditCnt	= len(spaceAuditList) 
	if spaceAuditCnt > 0:
		spaceAudits		= "<br /><ul>"
		
		# remove the blank lines in notes, as it stuffs up the renering of points on the map
		for i in spaceAuditList:
			if i.notes == None: 
				i.notes = ""
				i.save()
			# end if
			i.notes		= i.notes.replace("\n", '')
			i.notes		= i.notes.replace("\r", '')
			i.notes		= i.notes.replace("\t", '')
			mapLat		= i.owner.latitude
			mapLong		= i.owner.longitude
			spaceAudits	+= "<li>" + i.notes + "</li>"  
		# next i
		
		spaceAudits		+= "</ul><br />"
	else:
		spaceAudits		= None
	# end if
	
	# SERVICE
	serviceAuditList	= mySession.serviceaudit_set.all()
	serviceAuditCnt		= len(serviceAuditList)
	if serviceAuditCnt > 0:
		serviceAudits	= "<br /><ul>"
		
		# remove the blank lines in notes, as it stuffs up the rendering
		for i in serviceAuditList:
			if i.notes == None:   ######BUG! this was !=
				i.notes = ""
				i.save()
			# end if
			i.notes		= i.notes.replace("\n", '')
			i.notes		= i.notes.replace("\r", '')
			i.notes		= i.notes.replace("\t", '')
			mapLat		= i.owner.latitude
			mapLong		= i.owner.longitude
			serviceAudits	+= "<li>" + i.notes + "</li>"  
		# next i
		
		serviceAudits	+= "</ul><br />"
	else:
		serviceAudits	= None
	# end if

	# LINK
	linkAuditList			= mySession.linkaudit_set.all()
	linkAuditCnt		= len(linkAuditList)
	if linkAuditCnt > 0:
		linkAudits		= "<br /><ul>"
		
		# remove the blank lines in notes, as it stuffs up the renering of points on the map
		for i in linkAuditList:
			if i.notes == None: 
				i.notes = ""
				i.save()
			# end if
			i.notes		= i.notes.replace("\n", '')
			i.notes		= i.notes.replace("\r", '')
			i.notes		= i.notes.replace("\t", '')
			mapLat		= i.owner.latitude
			mapLong		= i.owner.longitude
			linkAudits	+= "<li>" + i.notes + "</li>"  
		# next i
		
		linkAudits		+= "</ul><br />"
	else:
		linkAudits		= None
	# end if
	
	# ACCESS POINT
	accessPointAuditList	= mySession.accesspointaudit_set.all()
	accessPointAuditCnt		= len(accessPointAuditList)
	if accessPointAuditCnt > 0:
		accessPointAudits	= "<br /><ul>"
		
		# remove the blank lines in notes, as it stuffs up the renering of points on the map
		for i in accessPointAuditList:
			if i.notes == None: 
				i.notes = ""
				i.save()
			# end if
			i.notes		= i.notes.replace("\n", '')
			i.notes		= i.notes.replace("\r", '')
			i.notes		= i.notes.replace("\t", '')
			mapLat		= i.owner.latitude
			mapLong		= i.owner.longitude
			accessPointAudits	+= "<li>" + i.notes + "</li>"  
		# next i
		
		accessPointAudits	+= "</ul><br />"
	else:
		accessPointAudits	= None
	# end if
	
	sumAudits				= spaceAuditCnt + serviceAuditCnt + linkAuditCnt + accessPointAuditCnt
	
	# If there are audits, then report on them, otherwise report that there 
	# were none for this session
	if sumAudits:
		#########################################
		# create the figure for the page
		# changre this to get ratio of positive to negative audits
		#########################################
		# get stats of scores from 1 to 5
		scoreone = mySession.accesspointaudit_set.filter(score=1).count() + \
		          mySession.serviceaudit_set.filter(score=1).count() + \
		          mySession.linkaudit_set.filter(score=1).count() + \
		          mySession.spaceaudit_set.filter(score=1).count()
		scoretwo = mySession.accesspointaudit_set.filter(score=2).count() + \
		          mySession.serviceaudit_set.filter(score=2).count() + \
		          mySession.linkaudit_set.filter(score=2).count() + \
		          mySession.spaceaudit_set.filter(score=2).count()
		scorethree = mySession.accesspointaudit_set.filter(score=3).count() + \
		          mySession.serviceaudit_set.filter(score=3).count() + \
		          mySession.linkaudit_set.filter(score=3).count() + \
		          mySession.spaceaudit_set.filter(score=3).count()
		scorefour = mySession.accesspointaudit_set.filter(score=4).count() + \
		          mySession.serviceaudit_set.filter(score=4).count() + \
		          mySession.linkaudit_set.filter(score=4).count() + \
		          mySession.spaceaudit_set.filter(score=4).count()
		scorefive = mySession.accesspointaudit_set.filter(score=5).count() + \
		          mySession.serviceaudit_set.filter(score=5).count() + \
		          mySession.linkaudit_set.filter(score=5).count() + \
		          mySession.spaceaudit_set.filter(score=5).count()
		sumAudits = scoreone + scoretwo + scorethree + scorefour + scorefive
		
		scoreonePct		= scoreone / sumAudits
		scoretwoPct		= scoretwo / sumAudits
		scorethreePct		= scorethree / sumAudits
		scorefourPct	= scorefour / sumAudits
		scorefivetPct	= scorefive / sumAudits
		# draw a nice pie chart
		drawing = jrtC.JRTpieDrawing()
		drawing.pie.data 					= [scorefive, scorefour, scorethree, scoretwo, scoreone]
		drawing.pie.labels 					= ['Very Good', 'Good', 'Neutral', 'Bad', 'Very Bad']
		
		n = len(drawing.pie.data)
		jrtC.setItems(n, drawing.pie.slices,'fillColor', jrtC.pdf_chart_colors)
		drawing.legend.colorNamePairs 		= [(drawing.pie.slices[i].fillColor, \
											(drawing.pie.labels[i][0:20],\
											'%0.2f' % drawing.pie.data[i])) \
											for i in xrange(n)]
		
		# debugging is on my machine. In settings MEDIA_ROOT is set to static if on
		# my machine, but I could not set MEDIA_URL to STATIC_URL, as DJANGO does not
		# like this.
		if settings.PDFDEBUG:
			media_url						= settings.STATIC_URL
			media_root						= settings.STATICFILES_DIRS[0]
		else:
			media_url						= settings.MEDIA_URL
			media_root						= settings.MEDIA_ROOT
		
		# the drawing will be saved as pdf and png below, 
		# I should do this differently
		imgAnalysisPie						= "images/analysisPie"
		drawing.save(formats=['PDF',],outDir=media_root,fnRoot=imgAnalysisPie) # r171
		# execute the shell command to create the jpg
   		shellCom	= "convert -density 300 -trim " + media_root+ imgAnalysisPie + '.pdf '	
   		shellCom 	+= media_root + imgAnalysisPie + ".jpg"
   		# -resize " + str(jrtH.frame_width) + "x" 
   		# shellCom	+= str(10*jrtH.cm) + "
   		os.system(shellCom)
		# used by template
		figFileName							= imgAnalysisPie + ".jpg"	
	# end if
	
	return render_to_response('env_issues/audits.html', locals())	
	"""	DetailView.as_view(
				model=Session,
				template_name='env_issues/audits.html')"""
	
# end auditListReport

################################################################# 
# this is done more DRY in r130
# r203 showmap for objects
def showObjectmap(request, sessionId):
	# r130 include navigation here
	theNavigation	= staticVars.navigation

	# to calculate the centre position
	sumLat			= 0
	sumLong			= 0
	count			= 0
	
	# the login function checs for the session existing. No need to do it here
	mySession		= Session.objects.get(pk=sessionId)
	
	spaceList	= mySession.space_set.all()
	
	# remove the blank lines in notes, as it stuffs up the renering of points on the map
	for i in spaceList:
		if i.properties == None: 
			i.properties = ""
			i.save()
		# end if
		i.properties		= i.properties.replace("\n", ' ')
		i.properties		= i.properties.replace("\r", ' ')
		i.properties		= i.properties.replace("\t", ' ')
		mapLat		= i.latitude
		mapLong		= i.longitude
		count		+= 1
	# next i
	
	linkList	= mySession.link_set.all()
	
	# remove the blank lines in notes, as it stuffs up the renering of points on the map
	for i in linkList:
		if i.properties == None: 
			i.properties = ""
			i.save()
		# end if
		i.properties		= i.properties.replace("\n", ' ')
		i.properties		= i.properties.replace("\r", ' ')
		i.properties		= i.properties.replace("\t", ' ')
		mapLat		= i.latitude
		mapLong		= i.longitude
		count		+= 1
	# next i
	
	accesspointList = mySession.accesspoint_set.all()
	
	# remove the blank lines in notes, as it stuffs up the renering of points on the map
	for i in accesspointList:
		if i.properties == None: 
			i.properties = ""
			i.save()
		# end if
		i.properties		= i.properties.replace("\n", ' ')
		i.properties		= i.properties.replace("\r", ' ')
		i.properties		= i.properties.replace("\t", ' ')
		mapLat		= i.latitude
		mapLong		= i.longitude
		count		+= 1
	# next i
	
	serviceList = mySession.service_set.all()
	
	# remove the blank lines in notes, as it stuffs up the renering of points on the map
	for i in serviceList:
		if i.properties == None: 
			i.properties = ""
			i.save()
		# end if
		i.properties		= i.properties.replace("\n", ' ')
		i.properties		= i.properties.replace("\r", ' ')
		i.properties		= i.properties.replace("\t", ' ')
		mapLat		= i.latitude
		mapLong		= i.longitude
		count		+= 1
	# next i
	
	return render_to_response('env_issues/dynamic-objectmap.html', locals())
	
	
# end showObjectmap


################################################################# 
# this is done more DRY in r130
def showmap(request, sessionId):
	# r130 include navigation here
	theNavigation	= staticVars.navigation

	# to calculate the centre position
	sumLat			= 0
	sumLong			= 0
	count			= 0
	
	# the login function checs for the session existing. No need to do it here
	mySession		= Session.objects.get(pk=sessionId)
	
	spaceAuditList	= mySession.spaceaudit_set.all()
	
	# remove the blank lines in notes, as it stuffs up the renering of points on the map
	for i in spaceAuditList:
		if i.notes == None: 
			i.notes = ""
			i.save()
		# end if
		i.notes		= i.notes.replace("\n", '')
		i.notes		= i.notes.replace("\r", '')
		i.notes		= i.notes.replace("\t", '')
		mapLat		= i.owner.latitude
		mapLong		= i.owner.longitude
		count		+= 1
	# next i
	
	linkAuditList	= mySession.linkaudit_set.all()
	
	# remove the blank lines in notes, as it stuffs up the renering of points on the map
	for i in linkAuditList:
		if i.notes == None: 
			i.notes = ""
			i.save()
		# end if
		i.notes		= i.notes.replace("\n", '')
		i.notes		= i.notes.replace("\r", '')
		i.notes		= i.notes.replace("\t", '')
		mapLat		= i.owner.latitude
		mapLong		= i.owner.longitude
		count		+= 1
	# next i
	
	accesspointAuditList = mySession.accesspointaudit_set.all()
	
	# remove the blank lines in notes, as it stuffs up the renering of points on the map
	for i in accesspointAuditList:
		if i.notes == None: 
			i.notes = ""
			i.save()
		# end if
		i.notes		= i.notes.replace("\n", '')
		i.notes		= i.notes.replace("\r", '')
		i.notes		= i.notes.replace("\t", '')
		mapLat		= i.owner.latitude
		mapLong		= i.owner.longitude
		count		+= 1
	# next i
	
	serviceAuditList = mySession.serviceaudit_set.all()
	
	# remove the blank lines in notes, as it stuffs up the renering of points on the map
	for i in serviceAuditList:
		if i.notes == None: 
			i.notes = ""
			i.save()
		# end if
		i.notes		= i.notes.replace("\n", '')
		i.notes		= i.notes.replace("\r", '')
		i.notes		= i.notes.replace("\t", '')
		mapLat		= i.owner.latitude
		mapLong		= i.owner.longitude
		count		+= 1
	# next i
	
	return render_to_response('env_issues/dynamic-map.html', locals())
	
	
# end showmap

#################################################################
# r147
# The URL contains a json encrypted list of audit fields which
# are insterted into the audit table. The cgi audit.py was doing this
# before, and this works in the same way, though I check for sessions
# existing, audit.py did not, and as a result the foriegn key would
# have invalid values inserted. Mysql did not seem to stop this.
# The audio and photo still gets uploaded via CGI scripts.
# needs to be checked. have not put an entry in the knowledge base for this.
def audit(request, jsonAudit):
	########################
	# INITIALISE
	########################
	retVal				= {statusKey: ''}
	tableKey			= 'table'
	sessionKey			= 'session'
	ownerKey			= 'owner_id'
	typeKey				= 'type'
	standardKey			= 'standard_id'
	
	# it is not  compulsory to send this information
	conformsKey			= 'conforms'
	scoreKey			= 'score'
	notesKey			= 'notes'
	photoKey			= 'photo'
	audioKey			= 'audio'
	
	
	# The parameters are sent as a json encrypted string
	myParameters		= json.loads(jsonAudit)
	passedFields		= myParameters.keys() # not all fields will be passed
	
	# to use the DRY paradigm, define dictionaries for the tables
	myOwnerTables		= {'service': Service, 'link': Link, 'accesspoint': AccessPoint, \
						'space': Space}
	myAuditTables		= {'service': ServiceAudit, 'link': LinkAudit, 'accesspoint': AccessPointAudit, \
						'space': SpaceAudit}	
	myStandTables		= {'service': ServiceStandard, 'link': LinkStandard, \
						'accesspoint': AccessPointStandard, 'space': SpaceStandard}
	
	##########################
	# MAIN
	##########################
	# The session, table, standard and owner object must be sent
	if sessionKey not in passedFields or tableKey not in passedFields or \
		ownerKey not in passedFields or standardKey not in passedFields:
		retVal[statusKey]	+= "\nERROR: table, owner, session or standard was not passed\n"
		return HttpResponse(retVal)
	# end if
	
	# if the keys exist (above), then get the mandatory values
	mySession			= int(passedFields[sessionKey])
	myTable				= passedFields[tableKey]
	myOwner				= int(passedFields[ownerKey])
	myStandard			= int(passedFields[standardKey])
	
	# Get the session first
	try:
		mySession			= Session.objects.get(pk=mySession)
	except Session.DoesNotExist:
		retVal[statusKey]	= "\nERROR: Session %d does not exist\n" %mySession
		retVal				= json.dumps(retVal)
		return HttpResponse(retVal)
	# end try
	
	# then the object that owns the audit (that the audit belongs to)
	try:
		theOwner			= myOwnerTables['myTable'].objects.get(pk=myOwner)
	except myOwnerTables['myTable'].DoesNotExist:
		retVal[statusKey]	= "\nERROR: %s %d does not exist\n" %(myTable, myOwner)
		retVal				= json.dumps(retVal)
		return HttpResponse(retVal)
	# end try
	
	# now get the standard
	try:
		theStandard			= myStandTables['myTable'].objects.get(pk=myStandard)
	except myStandTables['myTable'].DoesNotExist:
		retVal[statusKey]	= "\nERROR: %sStandard %d does not exist\n" %(myTable, myStandard)
		retVal				= json.dumps(retVal)
		return HttpResponse(retVal)
	# end try
	
	
	
	# have to do this separately
	if conformsKey in passedFields:
		theAudit.conforms	= passedFields[conformsKey]
	# end if
	if scoreKey in passedFields:
		scoreKey.conforms	= passedFields[scoreKey]
	# end if
	if notesKey in passedFields:
		theAudit.notes	= passedFields[notesKey]
	# end if
	# %here% audit not finished
	
	scoreKey			= 'score'
	notesKey			= 'notes'
	photoKey			= 'photo'
	audioKey			= 'audio'
			
	myconforms				= passedFields[conformsKey]
	myScore					= passedFields[scoreKey]
	myNotes					= passedFields[notesKey]
			

# end audit

#################################################################
# r213
def webregister(request):
	
	rightNow			= datetime.datetime.now()
	
	myParticipant		= Participant()
	
	# if we submited the form
	if request.method == 'POST':
		form			= registerFormWeb(request.POST, instance=myParticipant)
		if form.is_valid():
			cd			= form.cleaned_data 
			# get the session name, and convert it to a session. It would have
			# been checked in the form as to validity
			mySessNm	= cd['email']
			if mySessNm:
				# r213
				# first get/create the session
				try:
					mySession			= Session.objects.get(name__exact = mySessNm)
				except Session.DoesNotExist:
					mySession = Session(start=datetime.datetime.now(), name=mySessNm)
					mySession.save()
					#  email user that their session has been created
					emailMsg			= """This email is being sent to confirm that you have successfully registered 
		with the liveability program, and your user name and session name is the 
		same as your email address, that is '%s'.
			A YouTube video on how to use the application is available at 
		'http://youtu.be/FglrwEdVhyY'. and further information on the project 
		is on our web site" 'http://www.liveable.unsw.edu.au'.
			Sincerely
					The Liveability Team""" %mySessNm
				
					# don't want to flag a 500 error on fail, but I should check or log some other way. fail_silently=True
					send_mail("You have successfully registered", emailMsg, 'The Liveability Project', \
						[mySessNm], fail_silently=True)
				# end try
				
				fb				= form.save()
				fb.session.add(mySession)
				fb.save()
			else:
				form.save()
			# end if
			
			# tell the user it has been submitted thanks
			myResponse = "You have registered successfully<BR>"
			myResponse += "<a href='/'>Return</a>"
			return HttpResponse(myResponse)
		# end if
	else:
		form			= registerFormWeb(instance=myParticipant)
	# end if
	
	return render_to_response('env_issues/register_form.html', locals(), \
			context_instance=RequestContext(request))
			
# end webregister

#################################################################
# r166 return the fields to be presented for registration. Mark them
# compulsory or optional. This would be better implemented as the same function 
# that handles registration, but I am unsure how to handle the parameters in 
# a homogonous way when the uses of the function are different
def registrationFields(request):
	retVal				= {statusKey: ''}
	
	# r213 get the compulsory fields from the form
	regForm				= registerForm()
	compFields			= [] # list of compulsory fields
	optFields			= [] # list of optional fields
	for fld in regForm.fields.keys():
		fldDef			= regForm[fld]
		if fldDef.field.required:
			compFields.append(fldDef.label)
		else:
			optFields.append(fldDef.label)
		# end if
	# next fld

	# the fieldList for the passed parameters are constants in settings
	# r186 need prompts
	retVal['compulsory']	= compFields
	retVal['optional']		= optFields
	
	retVal					= json.dumps(retVal)
	return HttpResponse(retVal)
	
# end registrationFields

#################################################################
# Take the user's email and try to create a participant with this email. If 
# already exists, return an error message to this effect
# r166 major change where the compulsory fields are dictated by the variable
# in settings.py. Also function above. THE EMAIL MUST BE SENT THOUGH
def register(request, jsonUser):
	statusKey			= 'status'
	statusIDkey			= 'statusID'
	# r188 need to use lower case for v1 app compatibility emailKey			= 'Email' # r186 email has upper case letter
	emailKey			= 'email'
	
	# if the status ID is null, then everything is okay. new in r166
	retVal				= {statusIDkey: 0}
	retVal[statusKey]	= ''
	
	# The parameters are sent as a json encrypted string
	myParameters		= json.loads(jsonUser)
	
	
	# to get the prompts working I need to convert the keys to the field
	# names here and create a new dictionary structure with the jsonUser variable
	# I do this by using a django form
	myRegForm			= registerForm()
	# convert the field label keys to field name keys
	for fld in myRegForm.fields:
		fldDef			= myRegForm[fld]
		# if the field label has been used as a key, then make the field name the key also
		if (fldDef.label in myParameters.keys()):
			myParameters[fld] = myParameters[fldDef.label]
		# end if
	# next fld
	
	passedFields		= myParameters.keys() # not all fields will be passed
	
	##########################
	# MAIN
	##########################
	# The email address must be passed r213 v1 of the app sends field name, v2 sends label
	if (emailKey not in passedFields):
		retVal[statusKey]	+= "\nERROR: Email address was not passed\n"
		retVal[statusIDkey]	= 1
	else:
		
		# first get/create the session
		try:
			mySession			= Session.objects.get(name__exact = myParameters[emailKey])
		except Session.DoesNotExist:
			mySession = Session(start=datetime.datetime.now(), name=myParameters[emailKey])
			mySession.save()
			# r178 email user that their session has been created
			emailMsg			= """This email is being sent to confirm that you have successfully registered 
with the liveability program, and your user name and session name is the 
same as your email address, that is '%s'.
	A YouTube video on how to use the application is available at 
'http://youtu.be/FglrwEdVhyY'. and further information on the project 
is on our web site" 'http://www.liveable.unsw.edu.au'.
	Sincerely
			The Liveability Team""" %myParameters[emailKey]
		
			# don't want to flag a 500 error on fail, but I should check or log some other way. fail_silently=True
			send_mail("You have successfully registered", emailMsg, 'The Liveability Project', \
				[myParameters[emailKey]], fail_silently=True)
		# end try
		
		# check if the participant exists
		# first the email
		try:
			myParticipant		= Participant.objects.get(email__exact = myParameters[emailKey])
		except Participant.DoesNotExist:
			# create one
			myParticipant		= Participant()
			# fld is the field name, optional fields first
			# r186
			for fld in settings.OPTIONAL_REGISTRATION_PROMPTS:
				if fld in passedFields:
					# r186 the two lists are in sync
					#fldIndex	= settings.OPTIONAL_REGISTRATION_PROMPTS.index(fld)
					#fieldName	= settings.OPTIONAL_REGISTRATION_FIELDS[fldIndex]
					# The prompts has not been implemented yet. I need some time to do properly
					fieldName	= fld
					setattr(myParticipant, fieldName, myParameters[fld])
				# end if
			# next fld
			
			# now the compulsory fields 
			for fld in settings.COMPULSORY_REGISTRATION_FIELDS:
				if fld in passedFields:
					# r180 gender is read from the application as a string. I have to 
					# convert it to a gender object
					# r186
					# r186 the two lists are in sync
					#fldIndex	= settings.OPTIONAL_REGISTRATION_PROMPTS.index(fld)
					#fieldName	= settings.OPTIONAL_REGISTRATION_FIELDS[flndIndex]
					# The prompts has not been implemented yet. I need some time to do properly
					fieldName	= fld
					if fieldName.lower() == "gender":
						# Base the gender on the first letter only
						myGender		=  myParameters[fld][0]
						if myGender.lower() == "m":
							setattr(myParticipant, fieldName, "M")
						else:
							setattr(myParticipant, fieldName, "F")
						# end if
					else: # not a gender object		
						setattr(myParticipant, fieldName, myParameters[fld])
					# end if 
					
				# else: # r171 compulsory field check is only done on the application
# 					# if the compulsory field was not passed, then exit with an error
# 					retVal[statusKey]	+= "\nERROR: Compulsory field '%s' was not passed\n" %fld
# 					retVal[statusIDkey]	= 2
# 					break
# 				# end if
			# next fld
			
			# save the participant if everything okay
			if not(retVal[statusIDkey]):
				myParticipant.save()
			# end if
		# end try
		
		if not(retVal[statusIDkey]):
			# now link it with the sessison
			myJoin				= Participant_Session(participant = myParticipant, session = mySession)
			myJoin.save()
			
			retVal[statusKey]	+= '\nSession linked with participant'
			retVal['session']	= mySession.id
		# end if
	
	# end if email address not passed
	
	# convert to JSON format
	retVal				= json.dumps(retVal)
	return HttpResponse(retVal)
# end register

###############################################################################
# r142 singleUserLogin like get session gets the session ID along with the participant it belongs to
def singleUserLogin(request, jsonUser):
	# the keys for the returned parameters
	emailKey			= 'email'
	
	# The parameters are sent as a json encrypted string
	myParameters		= json.loads(jsonUser)
	passedFields		= myParameters.keys() # not all fields will be passed
	
	# The email address must be passed
	if emailKey not in passedFields:
		retVal[statusKey]	+= "\nERROR: Email address was not passed\n"
	else:
		userEmail			= myParameters[emailKey]
		userName			= userEmail
		
		# Thoug this is a many to many relationship, the users individual session
		# will be named after his username, and there will only be one of this kind
		theSession			= get_object_or_404(Session, name__iexact=userEmail)
		
		# multi user sessions will not have a participant found this way.
		theParticipant		= get_object_or_404(Participant, email__iexact=userEmail)
		
		retVal				= {}
		
		# fld is the field name, idx is the index position
		for idx, fld in enumerate(theParticipant._meta.get_all_field_names()):
			try:
				# The session field is a foriegn key pointing to a record
				if fld == 'session':
					retVal[fld]		= theSession.id
					# r144
					retVal['start'] = str(theSession.start)
					# The number of audits made in this session
					# get the count of audits for this session (remember to use lower case)
					spAu	 		= theSession.spaceaudit_set.count()
					liAu			= theSession.linkaudit_set.count()
					apAu			= theSession.accesspointaudit_set.count()
					seAu			= theSession.serviceaudit_set.count()
					retVal['cntSpAu'] = spAu
					retVal['cntLiAu'] = liAu
					retVal['cntApAu']	= apAu
					retVal['cntSeAu'] = seAu
					# get the count of objects for this session (remember to use lower case)
					sp	 			= theSession.space_set.count()
					li				= theSession.link_set.count()
					ap				= theSession.accesspoint_set.count()
					se				= theSession.service_set.count()
					retVal['cntSp'] = sp
					retVal['cntLi'] = li
					retVal['cntAp']	= ap
					retVal['cntSe'] = se
				else:
					retVal[fld]		= getattr(theParticipant, fld)
				# end if
			except AttributeError:
				retVal[fld]		= None
			# end try
		# next fld
		
	# end if
	
	# convert to JSON format
	retVal				= json.dumps(retVal)
	return HttpResponse(retVal)
	
# end get_session

##################################################################
# r144 
# return objects within a certain distance to the passed latitude and
# longitude
######
# Passed Parameters:
# Must be sent
# lat, long:	the latitude and longitude of the location of interest
# table: What sort of object to return, either space, service, link or accesspoint
# optoinal:
# dist: objects are returned within this distance in meters. Default 100m
##################################################################
def retCloseObjects(request, jsonParms):
	# The parameters are sent as a json encrypted string
	myParms				= json.loads(jsonParms)
	passedParms			= myParms.keys() # not all fields will be passed
	
	# the returned information
	retVal		= {}
	statusKey	= 'status'
	
	latKey		= 'lat'
	longKey		= 'long'
	tableKey	= 'table'
	distKey		= 'dist'
	audioKey	= 'audio'
	photoKey	= 'photo'
	
	# dictionary of tables. Make sure the keys are all lower case
	tableDict	= {'space': Space, 'link': Link, 'accesspoint': AccessPoint, 'service': Service}
	
	
	# get the parameters
	# Must have latitude, longitude and Table
	if latKey in passedParms and longKey in passedParms and tableKey in passedParms:
		myLat	= myParms[latKey]
		myLong	= myParms[longKey]
		myTable	= myParms[tableKey].lower() # put it in lower case to match the keys
	else:
		retVal[statusKey]	= 'ERROR: lattitude, longitude or table not sent'
		return HttpResponse(retVal)
	# end if
		
	if distKey in passedParms:
		myDist		= myParms[distKey]
	else:
		# default
		myDist		= 100.0
	# end if
	
	# get the latitude difference and longitude difference to be within a radius
	# of the distance given
	(maxLatDiff, maxLongDiff)	= latLongDiff(myLat, myLong, myDist)

	# filter all objects within maxLatDiff and maxLongDiff
	theCloseObjects				= tableDict[myTable].objects.filter(latitude__lt= (myLat+maxLatDiff) \
								).filter(latitude__gt= (myLat-maxLatDiff) \
								).filter(longitude__lt= (myLong+maxLongDiff) \
								).filter(longitude__gt= (myLong-maxLongDiff) )
	
	# make the django records into a list of python dictionaries
	retVal						= []
	for i in theCloseObjects:
	
		# r186 ANy datetime needs to be converted to string before it can be
		# JSON serialised
		i.entered				= str(i.entered)
	
		a						= model_to_dict(i)
		# make sure the audio and photo files are urls
		if audioKey in a.keys():
			try:
				a[audioKey]				= a[audioKey].url
			except ValueError:
					a[audioKey]		= None
			# end try
		# endif
		if photoKey in a.keys():
			try:
				a[photoKey]				= a[photoKey].url
			except ValueError:
					a[photoKey]		= None
			# end try
		# endif
		# now append to the list of dicts
		retVal.append(a)
	# next i
	
	
	# Now put it in JSON format
	retVal						= json.dumps(retVal)
	
	# and return it
	return HttpResponse(retVal)
	
# end retCloseObjects



##################################################################
# r144 
# Show audits within a certain distance to the passed latitude and
# longitude on the map
######
# Passed Parameters:
# Must be sent
# lat, long:	the latitude and longitude of the location of interest
# table: What sort of object to return, either space, service, link or accesspoint
# optoinal:
# dist: objects are returned within this distance in meters. Default 100m
##################################################################
def showCloseAudits(request, jsonParms):
	# The parameters are sent as a json encrypted string
	myParms				= json.loads(jsonParms)
	passedParms			= myParms.keys() # not all fields will be passed
	
	# the returned information
	retVal		= {}
	statusKey	= 'status'
	
	latKey		= 'lat'
	longKey		= 'long'
	distKey		= 'dist'
	audioKey	= 'audio'
	photoKey	= 'photo'
	enteredKey	= 'entered'
	sessionKey	= 'session'
	
	# dictionary of tables. Make sure the keys are all lower case
	tableDict	= {'space': Space, 'link': Link, 'accesspoint': AccessPoint, 'service': Service}
	tableAudit	= {'space': SpaceAudit, 'link': LinkAudit, 'accesspoint': AccessPointAudit,\
				'service': ServiceAudit}

	# get the parameters
	# Must have latitude, longitude and Table
	if latKey in passedParms and longKey in passedParms:
		myLat	= myParms[latKey]
		myLong	= myParms[longKey]
	else: # 
		retVal[statusKey]	= 'ERROR: lattitude, longitude or table not sent'
		return HttpResponse(retVal)
	# end if
		
	if distKey in passedParms:
		myDist		= myParms[distKey]
	else:
		# default
		myDist		= 100.0
	# end if
	
	if sessionKey in passedParms: 
		mySession	= get_object_or_404(Session, pk=myParms[sessionKey])
	# end if
	
	# get the latitude difference and longitude difference to be within a radius
	# of the distance given
	(maxLatDiff, maxLongDiff)	= latLongDiff(myLat, myLong, myDist)

	# filter all objects within maxLatDiff and maxLongDiff
	spaceList			= Space.objects.filter(latitude__lt= (myLat+maxLatDiff) \
								).filter(latitude__gt= (myLat-maxLatDiff) \
								).filter(longitude__lt= (myLong+maxLongDiff) \
								).filter(longitude__gt= (myLong-maxLongDiff) )
	linkList			= Link.objects.filter(latitude__lt= (myLat+maxLatDiff) \
								).filter(latitude__gt= (myLat-maxLatDiff) \
								).filter(longitude__lt= (myLong+maxLongDiff) \
								).filter(longitude__gt= (myLong-maxLongDiff) )
	serviceList			= Service.objects.filter(latitude__lt= (myLat+maxLatDiff) \
								).filter(latitude__gt= (myLat-maxLatDiff) \
								).filter(longitude__lt= (myLong+maxLongDiff) \
								).filter(longitude__gt= (myLong-maxLongDiff) )
	accesspointList		= AccessPoint.objects.filter(latitude__lt= (myLat+maxLatDiff) \
								).filter(latitude__gt= (myLat-maxLatDiff) \
								).filter(longitude__lt= (myLong+maxLongDiff) \
								).filter(longitude__gt= (myLong-maxLongDiff) )
	count					= 0
	#
	spaceAuditList					= SpaceAudit.objects.filter(owner__in=spaceList)
	for a in spaceAuditList:
		if a.notes != None: # r210
			a.notes		= a.notes.replace("\n", '')
			a.notes		= a.notes.replace("\r", '')
			a.notes		= a.notes.replace("\t", '')
		# end if
		mapLat		= a.owner.latitude
		mapLong		= a.owner.longitude
		count		+= 1
	# next a
	
	linkAuditList					= LinkAudit.objects.filter(owner__in=linkList)
	for a in linkAuditList:
		if a.notes != None: # r210
			a.notes		= a.notes.replace("\n", '')
			a.notes		= a.notes.replace("\r", '')
			a.notes		= a.notes.replace("\t", '')
		# end if
		mapLat		= a.owner.latitude
		mapLong		= a.owner.longitude
		count		+= 1
	# next a
	
	serviceAuditList				= ServiceAudit.objects.filter(owner__in=serviceList)
	for a in serviceAuditList:
		if a.notes != None: # r210
			a.notes		= a.notes.replace("\n", '')
			a.notes		= a.notes.replace("\r", '')
			a.notes		= a.notes.replace("\t", '')
		# end if
		mapLat		= a.owner.latitude
		mapLong		= a.owner.longitude
		count		+= 1
	# next a
	
	accesspointAuditList			= AccessPointAudit.objects.filter(owner__in=accesspointList)
	for a in accesspointAuditList:
		if a.notes != None: # r210
			a.notes		= a.notes.replace("\n", '')
			a.notes		= a.notes.replace("\r", '')
			a.notes		= a.notes.replace("\t", '')
		# end if
		mapLat		= a.owner.latitude
		mapLong		= a.owner.longitude
		count		+= 1
	# next a
	
	return render_to_response('env_issues/dynamic-map.html', locals())
	
# end retCloseAudits

######################################################
# r148 
# this function is passed an object type and
# returns a list of subtypes associated with the object type
def listTypes(request, jsonParms):
	# The parameters are sent as a json encrypted string
	myParms				= json.loads(jsonParms)
	# Get the passed parameter
	objTyp				= myParms['objectType']
	
	# the tables are determined by the category sent
	typTables			= {'space' : SpaceType, 'service' : ServiceType, \
						'link': LinkType, 'accesspoint': AccessPointType}
	
	# the returned information
	retVal				= {}
	# key for returned values
	statusKey			= 'status'
	
	# get the subtype for the object type passed
	types4obj			= typTables[objTyp].objects.all()
	
	# make a list of dictionaries
	retVal				= []
	for i in types4obj:
		retVal.append(model_to_dict(i))
	# next i
	
	# now get the json dump for it
	retVal				= json.dumps(retVal)
	
	return HttpResponse(retVal)

# end listTypes

######################################################
"""def upload((request)
	if request.method == 'POST':
		form		= updateForm(request.POST, request.FILES)
		if form.is_valid():
			cd				= form.cleaned_data
			if 'filename' in cd.keys():
				mySpace.docfile = cd['filename']
			# end if
			
			mySpace.save()
			return HttpResponse("The file was saved")
		# end if
	# end if
	
	return HttpResponse("The upload function did not do its stuff")
# end upload"""
	

##################################################################
# r149
# make a new object
# Description: passed table name and fields in JSON format
# via HTTP POST. The table is extracted, and the fields are
# stored in key:value pair format. The table is then updated
# in the built database.
# At this stage, every post to this page inserts a record into
# the appropriate object table. Updates are not performed.
def newObject(request, jsonParms):
	# The parameters are sent as a json encrypted string
	myParms				= json.loads(jsonParms)
	# Get the passed parameter
	objTyp				= myParms['table']
	
	# the tables are determined by the category sent
	myTables			= {'space' : Space, 'service' : Service, \
						'link': Link, 'accesspoint': AccessPoint}
	typTables			= {'space' : SpaceType, 'service' : ServiceType, \
						'link': LinkType, 'accesspoint': AccessPointType}
						
	# the returned information
	retVal				= {}
	# key for returned values
	statusKey			= 'status'
	
	# compulsory passed keys
	nameKey				= 'name'
	typeKey				= 'type'
	latKey				= 'latitude'
	longKey				= 'longitude'
	sessionKey			= 'session'
	compKeys			= [nameKey, typeKey, latKey, longKey, sessionKey]
	
	# the IDs of foreign keys that are to be translated to records of relational tables
	foreignKeys			= [typeKey, sessionKey]
	# relational tables for the above
	relTables			= {}
	
	# first the type table
	relTables[typeKey]	= typTables[objTyp]

	
	# and the session relational field
	relTables[sessionKey]	= Session
	
	# an object must at least have these keys
	for k in compKeys:
		if not(k in myParms.keys()):
			retVal[statusKey] = 'ERROR: compulsory keys %s not passed.' %k
			retVal			= json.dumps(retVal)
			return HttpResponse(retVal)
		# end if
	# next k
	
	# get the relational record for all relational tables
	for rt in relTables.keys():
		try:
			relRec			= relTables[rt].objects.get(pk=myParms[rt])
		except relTables[rt].DoesNotExist:
			retVal[statusKey] = "ERROR: Creating %s ID = %d does not exist for relation '%s'" \
				%(objTyp, myParms[rt], rt)
			retVal			= json.dumps(retVal)
			return HttpResponse(retVal)
		# end try
		
		# now exchange the ID for the record so it can be used to create the new object
		myParms[rt]			= relRec
		
	# next rt
		
	# create a new ojbect
	newObj				= myTables[objTyp]()
	
	# for all the object's fields, if they match a passed parameter,
	# add them to the new object
	for idx, fld in enumerate(myTables[objTyp]._meta.get_all_field_names()):
		if fld in myParms.keys():
			# setattr is a function that will set the attribute given by the string (fld in this case)
			setattr(newObj, fld, myParms[fld])
		# end if
	# next fld
	
	# the date this object was created
	newObj.entered			= datetime.datetime.now()
	
	newObj.save()	
	
	retVal[statusKey]		= 0 # success
	retVal					= json.dumps(retVal)
	return HttpResponse(retVal)

# end newObject

##################################################################
# r175
# returns the message text from the database when passed an identifier for that text
# used as a database of help text for the application.
def getMessage(request, msgID):
	theMessage				= get_object_or_404(message, identifier=msgID)
	return HttpResponse(theMessage.information)
# end getMessage

##################################################################
# r142
# return a python list of dictionaries
def makeDicts(objList):
	objDict					= [] 
	for i in objList:
		myDict				= {}
		myDict['id']		= i.id
		
		# fld is the field name, idx is the index position
		for idx, fld in enumerate(i._meta.get_all_field_names()):
			
			# return the url for audio and photo fields
			if fld == 'audio' or fld == 'photo':
				try:
					myDict[fld]		= getattr(i, fld).url
				except ValueError:
					myDict[fld]		= None
				# end try
			elif 'ForeignKey' in str(getattr(i, fld).__class__): # put all foriegn keys here
				try:
					myDict[fld]			= getattr(i, fld).id
				except AttributeError:
					myDict[fld]		= None
				# end try
				# r147 hack to fix bug where parent field causes an error
			elif fld[:6] == 'parent':
				myDict[fld] = None
			else:
				try:
					myDict[fld]		= getattr(i, fld)
				except AttributeError:
					myDict[fld]		= None
				# end try
			# end if
			
		# next fld
		
		objDict.append(myDict)
	# next i
	
	return objDict
# end makeDicts

##################################################################
# r144 Given 2 GPS positions return the distance in kms
def gpsDistM(lat1, long1, lat2, long2):
	
	# phi = 90 - lattitude
	phi1			= (90.0 - lat1)*settings.DEG2RAD
	phi2			= (90.0 - lat2)*settings.DEG2RAD
	
	# theta = longitude
	theta1			= long1*settings.DEG2RAD
	theta2			= long2*settings.DEG2RAD
	
	# compute spherical distance from spherical coordinates
	# For two locations in spherical coordinates
	# (1, theta,1 phi1) and (1, theta2, phi2)
	# cos( arc length ) = sin phi1 sin phi2 * cos(theta1 - theta2) + 
	#	cos phi1 cos phi2
	# distance = rho * arc length
	
	cosArc			= sin(phi1) * sin(phi2) * cos(theta1 - theta2) + \
					cos(phi1) * cos(phi2)
	arcLen			= acos( cosArc )
	
	# mutiply by arc radius of the earth in kilomiters
	arcLen			= arcLen * settings.EARTHRADIUS
	
	return arcLen
# end gpsDistM

######################################################
# J1.1 return the difference in latitude and longitude as a tuple given
# a distance. This means that at the given location the maximum difference
# in latitude and longitude are these numbers
def latLongDiff(lat1, long1, dist):
	# distance must be floating point
	dist			= float(dist)
	# unit distance is relative to the unit sphere
	unitDist		= dist / settings.EARTHRADIUS
	myLambda		= cos(unitDist)

	# perform the inverse function of gpsDistM
	# NOTE I do not check for a zero denominator.
	# latitude difference is just the distance
	latDiff			= unitDist * settings.RAD2DEG

	# longitude
	#myAngle			= (2*myLambda - cos(2.0*long1*settings.DEG2RAD) - 1) / (1 - cos(2.0*long1*settings.DEG2RAD))
	#longDiff		= abs(acos(myAngle))
	myRad			= settings.EARTHRADIUS * cos(lat1*settings.DEG2RAD)
	longDiff		= (dist / myRad) * settings.RAD2DEG

	return (latDiff, longDiff)

# end latLongDiff

######################################################
def testPDF(request):
	import JRTreportlabHTML as jrt
	import tempfile

	file = tempfile.NamedTemporaryFile()

	e = jrt.PdfA4Letter(file.name)

	ref = settings.MEDIA_ROOT + 'liveability_logo.png'
	e.image(ref, width=jrt.frame_width*0.25, height=10*jrt.cm)
	e.h1(u'My Heading one')
	e.text("""
	Directors at Daimler Benz and Chrysler have announced an agreement to adopt
English as the preferred language for communications, rather than German, which
was another possibility. As part of the negotiations, directors at Chrysler
conceded that English spelling has some room for improvement and have accepted a
five-year phase-in plan. In the first year, "s" will be used instead of the soft
"c". Also, the hard "c" will be replased with "k". Not only will this klear up
konfusion, but komputers have one less letter. There will be growing kompany
enthusiasm in the sekond year when the troublesome "ph" will be replased by "f".
This will make words like "fotograf" 20 persent shorter. In the third year,
DaimlerKhrysler akseptanse of the new spelling kan be expekted to reash the
stage where more komplikated shanges are possible. DaimlerKhrysler will
enkourage the removal of double letters, whish have always ben a deterent to
akurate speling. Also, al wil agre that the horible mes of silent "e"'s in the
languag is disgrasful, and they would go. By the fourth year, peopl wil be
reseptiv to steps sush as replasing "th" with "z" and "w" by "v". During ze fifz
year, ze unesesary "o" kan be droped from vords kontaining "o", and similar
shanges vud of kors be aplid to ozer kombinations of leters. After zis fifz yer,
ve vil hav a reli sensibl riten styl. Zer vil be no mor trubls or difikultis,
and employes vil find it ezi to kommunikat viz eash ozer. Ov kors al supliers
vil be expekted to us zis for all busines komunikation via DaimlerKhrysler. Ze
drem vil finali kum tru. Und efter ze fifz yer, ve vil al be speking German like
zey vunted in ze forst plas. If zis mad yu smil, plez pas on to oza pepl. 
	""")
	e.h3('My Heading three')

	t = """
	ascasc<br />
	ascascasc<br />
	<ul>
		<li>sdv1</li>
		<li>sdv2</li>
		<li>sdv3</li>
	</ul>
	ascasc<br />
	ascasc<br />
	"""

	e.text(t)
	e.blankline(2)
	e.end_keep_together()
	e.build()

	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=gugus.pdf'
	response.write(file.read()) 
	file.close()
	return response	

# end testPDF

##################################################################
# test the functionality of email
def testEmail(request):
	theEmail		= """Hello,
	I am writing an email to you as a bit of a test. This is from the built env system
	I hope you like my email. Or at least are happy in that recieving it proves that 
	it works.
		Sincerely
			Bot, as in Robot."""
			
	send_mail("This is a serious subject", theEmail, 'ITMS Job System', \
				['jrthorne@jrtdatasol.com'], fail_silently=False)
				
	myMsg 			= "<H1>You have emaield yoruself<H1>"
	return HttpResponse(myMsg)

# end testEmail	
