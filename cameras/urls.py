from django.urls import path 

from .views import *

urlpatterns = [
       path("shared-cameras/", SharedCameraList.as_view()),
       path('camera_live/<int:camera_id>/',CameraRetrive.as_view())
]
