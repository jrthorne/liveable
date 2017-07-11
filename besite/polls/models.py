import datetime

from django.db import models

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pubDate = models.DateTimeField('date published')

	# for printing 
	def __unicode__(self):
		return self.question
	# end unicode

	def wasPublishedRecently(self):
		return self.pubDate >=datetime.datetime.now() - datetime.timedelta(days=1)
	# end wasPublishedRecently
# end class

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	# for printing 
	def __unicode__(self):
		return self.choice
	# end unicode
# end class


