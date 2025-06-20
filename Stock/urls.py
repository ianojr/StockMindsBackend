from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^stock/$', views.StockApi),
    re_path(r'^stock/(?P<id>\d+)/$', views.StockApi),
]
