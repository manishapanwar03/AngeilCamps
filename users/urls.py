from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path 
from .views import *

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('sign-up/',SignUp.as_view()),
    path('personal-token/', PersonalTokenView.as_view()),
    path('personal-token/<int:pk>/', PersonalTokenView.as_view(), name='personal-token-detail'),
    
]
