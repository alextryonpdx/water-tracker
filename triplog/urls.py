from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.entries_list, name='entries_list'),
]