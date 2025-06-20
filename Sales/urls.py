from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^sales/$', views.SaleApi),
    re_path(r'^sales/(?P<id>\d+)/$', views.SaleApi),
]
