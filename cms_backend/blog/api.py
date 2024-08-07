from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Blog
from .serializers import BlogsListSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def blogs_list(request):
      blogs = Blog.objects.all()
      serializer = BlogsListSerializer(blogs, many=True)
 
      return JsonResponse({
            'data': serializer.data
      })