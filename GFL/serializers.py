
from rest_framework import serializers
from .models import Tournament,Admin_class

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        st = Admin_class.tournament_admin 
        fields = ['id', 'tournament_name', 'tournament_type','tournament_class','tournament_total_team','tournament_template','tournament_detials','lat','lon','start_date','end_date','admin']