from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^supplier/$', views.SupplierApi),
    re_path(r'^supplier/(?P<id>\d+)/$', views.SupplierApi),
]
