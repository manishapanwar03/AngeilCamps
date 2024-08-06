from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

import requests

#ANGELCAM_API_URL = "https://api.angelcam.com/v1"
#ANGELCAM_PAT = "5666540a04958735183a89b4263a0b86416aff04"  # Replace this with your PAT

ANGELCAM_API_URL = settings.ANGELCAM_API_URL

class SharedCameraList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ANGELCAM_PAT = request.headers.get('Authorization1')
        headers = {
            'Authorization': f'PersonalAccessToken {ANGELCAM_PAT}'
        }
        response = requests.get(f"{ANGELCAM_API_URL}/cameras", headers=headers)
       # response = requests.get(f"{ANGELCAM_API_URL}/shared-cameras/", headers=headers)
        if response.status_code == 200:
            camera_data = response.json().get('results', [])
            return JsonResponse(camera_data,safe=False)
        else:
            return Response(response.json(), status=response.status_code)
        

    

class CameraRetrive(APIView):
    def get(self,request,camera_id=None):
        ANGELCAM_PAT = request.headers.get('Authorization1')
        headers = {
            'Authorization': f'PersonalAccessToken {ANGELCAM_PAT}'
        }
        response = requests.get(f"{ANGELCAM_API_URL}/cameras/{camera_id}/", headers=headers)
        if response.status_code == 200:
            camera_data = response.json()
            return JsonResponse(camera_data,safe=False)
        else:
            return Response(response.json(), status=response.status_code)
