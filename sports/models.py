from django.db import models

# Create your models here.
class Team(models.Model):
    team=models.CharField(max_length=50)
    team_id=models.CharField(max_length=50)
    
class League(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    played=models.IntegerField()
    gd=models.IntegerField()
    points=models.IntegerField()
    

class Match(models.Model):
    week=models.IntegerField()
    date=models.DateField()
    home=models.IntegerField()
    away=models.IntegerField()
    status=models.CharField(max_length=50)
    score=models.CharField(max_length=50)
    league=models.ForeignKey(League,on_delete=models.CASCADE)

   