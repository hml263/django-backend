from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Team
from .serializers import TeamsListSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def teams_list(request):
      teams = Team.objects.all()
      serializer = TeamsListSerializer(teams, many=True)
 
      return JsonResponse({
            'data': serializer.data
      })