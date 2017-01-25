from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^login/$', auth_views.login,name='login'),
    url(r'^logout/$', auth_views.logout,name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login,name='logout_then_login'),

    url(r'^$', views.dashboard, name='dashboard'),

    # change password urls
    url(r'^password-change/$',auth_views.password_change,name='password_change'),
    url(r'^password-change/done/$',auth_views.password_change_done,name='password_change_done'),
]
