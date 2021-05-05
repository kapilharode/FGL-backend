
from django.urls import path
from . import views
urlpatterns = [
    path('tournamentapi/',views.ListTournament.as_view()),
    path('tournamentapi/<int:pk>/',views.ListTournament.as_view()),
    path('postadmin/',views.Post_admin.as_view()),
    path('listapi/<str:tournament_admin>',views.List_admin.as_view()),

]
