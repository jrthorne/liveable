from api_wikki.models import category, knowledge
from django.contrib import admin
import datetime


###############################################################
class knowledgeAdmin(admin.ModelAdmin):
	fields				= ['date_entered', 'title', 'category', 'description', 'docfile']
	list_display		= ['id', 'date_entered', 'entered_by', 'title', 'category']
	search_fields		= ['title', 'description']
	list_filter			= ['category', 'date_entered']
	
	ordering			= ['-date_entered']
	#prepopulated_fields = {'date_entered' : [datetime.datetime.now()]}
	
	# put in the entered_by field
	def save_model(self, request, obj, form, change):
		if not change:
			obj.entered_by = request.user
		# end if 
		obj.save()
	# end save_model
	
# end knowledgeAdmin

#####################################################################
class categoryAdmin(admin.ModelAdmin):
	fields				= ['name', 'description']
	list_display		= ['id', 'name']
# end categoryAdmin

#####################################################################
admin.site.register(knowledge, knowledgeAdmin)
admin.site.register(category, categoryAdmin)