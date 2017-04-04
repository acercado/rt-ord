from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^json_usagetypes/$', views.get_json_usagetypes, name='json_usagetypes'),
    url(r'^json_bcast_data/$', views.get_json_bcast_data, name='json_bcast_data'),
    url(r'^wizard/$', views.form_wizard, name='wizard'),
    url(r'^basic/$', views.basic_page, name='basic_page'),
    url(r'^test/$', views.test_page, name='test_page'),
]
