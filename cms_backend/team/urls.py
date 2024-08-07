from django.urls import path

from . import api


urlpatterns = [
    path('', api.teams_list, name='api_teams_list'),
   
  
   

]