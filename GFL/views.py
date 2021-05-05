from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from http.client import responses
from .models import Tournament,Admin_class
from .serializers import TournamentSerializer

class ListTournament(APIView):
   
    def get(self, request, format=None):
        '''
        tr = Tournament.objects.all()
        serializer = TournamentSerializer(tr, many = True)
     
        return Response(serializer.data)

        '''
        kj = Tournament.objects.all()
        result_data =[]
        for j in kj:
             result = {
                      "tournament_name": j.tournament_name,
                      "admin":j.admin.tournament_admin
                    }
             result_data.append(result)
          
        return Response(result_data)
        
        
    def post(self, request, format=None):
         '''
         serializer = TournamentSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            
            return Response({"msg":"create Tournament successfully"}) 

         '''

    
         tournament_name = request.data['tournament_name']
         tournament_type = request.data['tournament_type']
         tournament_class = request.data['tournament_class']
         tournament_total_team = request.data['tournament_total_team']
         tournament_template = request.data['tournament_template']

         tournament_detials = request.data['tournament_detials']
         lat = request.data['lat']

         lon = request.data['lon']
         start_date = request.data['start_date']
         end_date = request.data['end_date']
         Admin_class.tournament_admin = request.data['admin']
         k= Admin_class.tournament_admin

         tournament= Tournament.objects.create(tournament_name=tournament_name,tournament_type=tournament_type,tournament_class=tournament_class,
         tournament_total_team=tournament_total_team,tournament_template=tournament_template,tournament_detials =tournament_detials,
         lat=lat,lon=lon,start_date=start_date,end_date=end_date,admin=k)

         tournament.save()
         return Response({"msg":"create Tournament successfully"})
         


    def delete(self, request, pk, format=None):
        id = pk
        tr = Tournament.objects.get(pk=id)
        tr.delete()
        return Response({"msg":"Delete Tournament"})





class List_admin(APIView):
     def get(self,request,tournament_admin,format=None):
         admin_name = tournament_admin
         #name = request.data['admin']
         #admin_data= Tournament.objects.filter(admin= name)
         #tr = Tournament.objects.all()
         admin_data = Admin_class.objects.get(tournament_admin=admin_name)
         admin_filter_data = Tournament.objects.filter(admin=admin_data)

         #tr = Tournament.objects.all()
         serializer = TournamentSerializer(admin_filter_data, many = True)
     
         return Response(serializer.data) 


         """result_data =[]
         for j in kj:
             result = {
                      "tournament_name": j.tournament_name,
                      "tournament_class":j.tournament_class
                    }
             result_data.append(result)
          
         return Response(result_data)
         """
      
            
    
class Post_admin(APIView):

     def get(self,request,format=None):
         
         tr = Admin_class.objects.all()
         #serializer = TournamentSerializer(tr, many = True)
         admin_list =[]
         for task in tr:
             result = {
             "tournament_admin": task.tournament_admin,
             
             }
             admin_list.append(result)
         return Response(admin_list)
     
         

     def post(self, request, format=None):
       # serializer = TournamentSerializer(data=request.data)
       name = request.data['tournament_admin']
       admin_data = Admin_class.objects.create(tournament_admin=name)
       admin_data.save()
    
       return Response({"msg":"create admin successfully"})

         
