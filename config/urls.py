# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from allauth.account import views

urlpatterns = [
    # no landing page yet, so dis is thisabled
    # url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    
    # go directly to allauth's login
    url(r"^$", views.login, name="account_login"),
    url(r"^accounts/login", views.login, name="account_login"),
    
    url(r'^sampler$', TemplateView.as_view(template_name='base_main.html'), name='sampler'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('bcast_online_report_dashboard.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^usagetypes/', include('bcast_online_report_dashboard.usagetypes.urls', namespace='usagetypes')),
    url(r'^dashboard/', include('bcast_online_report_dashboard.dashboard.urls', namespace='dashboard')),
    url(r'^charts/', include('bcast_online_report_dashboard.charts.urls', namespace='charts')),
    url(r"^accounts/login", views.login, name="account_login"),
    url(r'^accounts/signup', views.signup, name="account_signup"),

    # Your stuff: custom urls includes go here
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
