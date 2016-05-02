from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.entries_list, name='entries_list'),
    url(r'^guides/$', views.guide_list, name='guide_list'),
    url(r'^guides/(?P<pk>\d+)/$', views.single_guide, name='single_guide'),
    url(r'^trips/(?P<pk>\d+)/$', views.single_trip, name='single_trip'),
	url(r'^guides/new/$', views.guide_new, name='guide_new'),
	url(r'^log/new/$', views.entry_form, name='entry_new'),
    # url(r'^guides/(?P<pk>\d+/(?S<pk>\d+/(?E<pk>\d+)/$', views.guide_new, name='guide_new'),
	url(r'^sort/$', views.SortView, name='sort_view'),
	url(r'^sorted/$', views.SortView, name='sorted_view'),
]