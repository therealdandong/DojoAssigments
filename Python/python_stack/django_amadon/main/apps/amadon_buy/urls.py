from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^amadon/$', views.index, name="amadon_index"),
    url(r'^amadon/process/$', views.process, name="amadon_process"),
    url(r'^amadon/result/$', views.result, name="amadon_result")
]