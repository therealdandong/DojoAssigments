from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="login_register"),
    url(r'^process_register', views.process_register, name="process_register"),
    url(r'^process_login', views.process_login, name="process_login"),
    url(r'^users/(?P<id>\d+)', views.users, name="user_page"),
    url(r'^books/add', views.add_all, name="add_all"),
    url(r'^books/add/process', views.add_all_process, name="add_all_process"),
    url(r'^books/(?P<id>\d+)',  views.add_book, name="add_book")
]