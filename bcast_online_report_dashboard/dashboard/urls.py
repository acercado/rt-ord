from django.conf.urls import url
from . import views
from allauth.account import views as olawt

urlpatterns = [
    url(r'^$', views.dashboard1, name='dashboard1'),
    # url(r"^accounts/login", views.login, name="account_login"),
    url(r"^accounts/login", olawt.login, name="account_login"),
    url(r'^panel1/', views.dashboard1, name='panel1'),
    url(r'^panel2/$', views.dashboard2, name='panel2'),
    url(r'^panel3/$', views.dashboard3, name='panel3'),
    url(r'^datatables/$', views.datatables, name='datatables'),
    
    url(r'^tester/$', views.tester, name='tester'),
]
