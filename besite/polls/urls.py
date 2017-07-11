from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template
from polls.models import Poll

urlpatterns = patterns('',
	url(r'^$', 
		ListView.as_view(
			queryset=Poll.objects.order_by('-pubDate')[:5],
			context_object_name='latestPollList',
			template_name='polls/index.html')),
	url(r'^(?P<pk>\d+)/$',
		DetailView.as_view(
			model=Poll,
			template_name='polls/detail.html')),
	url(r'^(?P<pk>\d+)/results/$', 
		DetailView.as_view(
			model=Poll,
			template_name='polls/results.html'),
		name='poll_results'),
	url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
	url(r'^about/$', direct_to_template, { \
		'template': 'about.html' \
	}),
)

