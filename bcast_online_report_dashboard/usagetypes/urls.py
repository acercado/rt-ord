from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^usagetypes/$', views.get_usagetypes, name='usagetypes'),
]
