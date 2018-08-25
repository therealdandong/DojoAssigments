from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="user_home"),
    url(r'^users$', views.index, name="user_home"),
    url(r'^users/new$', views.new, name="user_new"),
    url(r'^users/(?P<id>\d+)/show', views.show, name="user_show"),
    url(r'^users/create$', views.create, name="user_create"),
    url(r'^users/(?P<id>\d+)/update', views.update, name="user_update"),
    url(r'^users/(?P<id>\d+)/edit', views.edit, name="user_edit"),
    url(r'^users/(?P<id>\d+)/delete', views.delete, name="user_delete")
]