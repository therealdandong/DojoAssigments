from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home_page"),
    url(r'^process', views.process, name="user_process"),
    url(r'^validate', views.validate, name="user_validate"),
    url(r'^success/(?P<id>\d+)', views.success, name="user_success")
]
