from django.conf.urls import url
from.import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<register_id>[0-9]+)/$', views.detail,name='detail'),
    # url(r'^com1/(?P<id>[0-9]+)/$', views.complect,name='complect'),

    url(r'^$', views.index11, name='index'),
    url(r'^reg1/create$', views.create, name='create'),
    url(r'^join1/create1$', views.create1, name='create1'),
    url(r'^curr1/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^curr1/edit/update/(?P<id>\d+)$', views.update, name='update'),
    # url(r'^curr1/complect/(?P<id>\d+)$', views.complect, name='complect'),
    url(r'^curr1/comp1/(?P<id>\d+)$', views.complect, name='complect'),
    url(r'^curr1/delete/(?P<id>\d+)$', views.delete, name='delete'),





    url(r'^reg1/$',views.registers,name='registers'),
    url(r'^join1/$',views.joinings,name='joinings'),
    url(r'^walk1/$',views.walkins,name='walkins'),
    url(r'^curr1/$',views.currents,name='current'),

    url(r'^call1/$',views.callings,name='callings'),
    url(r'^call1/callings1$',views.callings1,name='callings1'),

    url(r'^coun1/$',views.counselling,name='counselling'),
    url(r'^coun1/counselling1$',views.counselling1,name='counselling1'),
    url(r'^coun1/counselling1/edit/(?P<id>\d+)$', views.edit1, name='edit1'),
    url(r'^coun1/counselling1/edit/update1/(?P<id>\d+)$', views.update1, name='update1'),
    url(r'^coun1/counselling1/delete1/(?P<id>\d+)$', views.delete1, name='delete1'),
    # url(r'^demo1/$',views.index1,name='registers1'),

    url(r'^st1/$',views.students,name='students'),
    # url(r'^st1/rejoin/(?P<id>\d+)$',views.editre,name='editre'),
    # url(r'^st1/rejoin/updatere/(?P<id>\d+)$', views.updatere, name='updatere'),

]

   

   