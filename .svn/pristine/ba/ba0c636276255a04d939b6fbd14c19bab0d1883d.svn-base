import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
###############################################################
class category(models.Model):
	name			= models.CharField(max_length=255)
	description		= models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name
	# end unicode
# end category
###############################################################
class knowledge(models.Model):
	category		= models.ForeignKey(category, null=True, blank=True)
	title			= models.CharField(max_length=255)
	description		= models.TextField()
	date_entered	= models.DateField()
	entered_by		= models.ForeignKey(User)
	docfile 		= models.FileField(upload_to='%Y%m%d', \
					null=True, blank=True)
	
	def __unicode__(self):
		return self.title
	# end unicode
# end knowledge