from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model		= Choice
	extra		= 3
# end choiceInline

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['question']}),
		('Date inforhoohee', {'fields': ['pubDate'], 
		'classes': ['collapse']}),
	]
	inlines				= [ChoiceInline]
	list_display		= ('question', 'pubDate', 'wasPublishedRecently')
	search_fields		= ['question']
	date_hierarchy		= 'pubDate'
# end PollAdmin

admin.site.register(Poll, PollAdmin)
