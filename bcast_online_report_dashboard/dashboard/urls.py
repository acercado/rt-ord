from django.conf.urls import url
from . import views
# from allauth.account import views

urlpatterns = [
    # url(r'/dasboard^$', views.dashboard1, name='dashboard1'),
    # url(r"^accounts/login", views.login, name="account_login"),
    url(r'^panel1/$', views.dashboard1, name='dashboard1'),
    url(r'^panel2/$', views.dashboard2, name='dashboard2'),
    url(r'^panel3/$', views.dashboard3, name='dashboard3'),
    url(r'^datatables/$', views.datatables, name='datatables'),
]
