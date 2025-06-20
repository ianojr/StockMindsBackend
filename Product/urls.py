from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^products/$', views.ProductApi),
    re_path(r'^products/(?P<id>\d+)/$', views.ProductApi),
]
