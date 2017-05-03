from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel1/$', views.charts_panel1, name='charts_panel1'),
]
