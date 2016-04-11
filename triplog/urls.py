from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.entries_list, name='entries_list'),
    url(r'^guides/$', views.guide_list, name='guide_list'),
    url(r'^guides/(?P<pk>\d+)/$', views.single_guide, name='single_guide'),
    url(r'^trips/(?P<pk>\d+)/$', views.single_trip, name='single_trip'),
]