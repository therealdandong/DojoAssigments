from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home_index"),
    url(r'^process', views.process, name="process_request")
]