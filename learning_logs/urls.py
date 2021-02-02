"""Define URL schemes for learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Homepage
    url(r'^$', views.index, name='index'),
    # All topics output
    url(r'^topics/$', views.topics, name='topics'),
]
