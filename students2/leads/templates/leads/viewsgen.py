from django.views import generic
from.models import Registers,Joinings

class IndexView(generic.ListView):
	template_name = 'leads/index.html'

	def get_queryset(self):
		return Registers.objects.all()

class DetailView(generic.DetailView):
	model - Registers
	template_name = 'leads/detail.html'

	def get_queryset(self):
		return Registers.objects.all()

#urls in apps
'''
from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),name='detail'),
]
------------------------------------

index.html
{% extends 'leads/test.html' %}


{% block body %}
	{% if all_registers %}

		<ul>
			{% for registers in object_list %}
				<li><a href="/leads/{{ registers.id }}/">{{ registers.st_name }}</a></li>
			{% endfor %}
		</ul>
	{% else %}
		<h3>you don't have any albums</h3>
	{% endif %}
{% endblock %}
-------------------------------
from django.views import generic
from.models import Registers,Joinings

class IndexView(generic.ListView):
	template_name = 'leads/index.html'
	context_object_name='all_registers'
	def get_queryset(self):
		return Registers.objects.all()

class DetailView(generic.DetailView):
	model - Registers
	template_name = 'leads/detail.html'

	def get_queryset(self):
		return Registers.objects.all()
----------------
{% extends 'leads/test.html' %}


{% block body %}
	{% if all_registers %}

		<ul>
			{% for registers in all_registers %}
				<li><a href="/leads/{{ registers.id }}/">{{ registers.st_name }}</a></li>
			{% endfor %}
		</ul>
	{% else %}
		<h3>you don't have any albums</h3>
	{% endif %}
{% endblock %}