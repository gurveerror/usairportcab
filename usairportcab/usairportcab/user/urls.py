from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    url(r'^$', views.user_login, name='login'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^add-car/$', views.addfare, name='add-car'),
    url(r'^edit-car-fare/(?P<id>\d+)$', views.editfare, name='editfare'),
    url(r'^delete-car-fare/(?P<id>\d+)$', views.deletecarfare, name='deletecarfare'),
    url(r'^edit-site-settings/$', views.sitesettings, name='sitesettings'),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/user/'}),
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]