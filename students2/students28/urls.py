from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
	url(r'^demo/',  include('leads.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^leads/', include('leads.urls')),
    url(r'^registers/', include('leads.urls')),
    url(r'^joinings/', include('leads.urls')),
    url(r'^walk/', include('leads.urls')),
    url(r'^current/', include('leads.urls')),
    url(r'^calling/', include('leads.urls')),
    url(r'^counselling/', include('leads.urls')),
    url(r'^complect/', include('leads.urls')),
    url(r'^students/', include('leads.urls')),

]
