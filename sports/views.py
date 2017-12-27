from django.shortcuts import render
from .models import Team
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TeamSerializer
import requests
# Create your views here.
class TeamInvetory(APIView):
    def get(self,request,format=None):
        '''
        simple api end for getting all teams from the Team model
        '''
        print("boom shaka laka")
        r = requests.get('http://127.0.0.1:3001/v2/teams')
        teams = r.json()
        team_json = teams["teams"]
        for team in team_json:
            team_name = team["team"]
            team_id = team["team_id"]
            print(team_name)
        print(len(teams["teams"]))
        all_teams = Team.objects.all()
        serializers = TeamSerializer(all_teams,many=True)
        return Response(serializers.data)