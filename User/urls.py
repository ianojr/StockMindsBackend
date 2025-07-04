from django.contrib import admin 
from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from .views import RegisterView, ProtectedView

urlpatterns = [ 
    path('register/', RegisterView.as_view(), name='register'), 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('protected/', ProtectedView.as_view(), name='protected'), 
]