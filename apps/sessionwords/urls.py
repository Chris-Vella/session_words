from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sessionwords$', views.sessionwords),
    url(r'^reset$', views.reset)
]