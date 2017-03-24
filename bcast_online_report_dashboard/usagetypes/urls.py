from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^usagetypes/$', views.usagetypes, name='usagetypes'),
]
