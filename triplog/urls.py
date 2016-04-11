from django.conf.urls import url
from . import views
from organizations.backends import invitation_backend

urlpatterns = [
    url(r'^$', views.entries_list, name='entries_list'),
    url(r'^guides/$', views.guide_list, name='guide_list'),
    url(r'^guides/(?P<pk>\d+)/$', views.single_guide, name='single_guide'),
    url(r'^trips/(?P<pk>\d+)/$', views.single_trip, name='single_trip'),
    #django-organizations
    url(r'^accounts/', include('organizations.urls')),
    url(r'^invitations/', include(invitation_backend().get_urls())),
]