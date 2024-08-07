from django.urls import path

from . import api


urlpatterns = [
    path('', api.blogs_list, name='api_blogs_list'),
   
  
   

]