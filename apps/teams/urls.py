from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.TeamApiView.as_view()),
    path('detail/<int:id_team>', views.TeamDetailView.as_view()),
    path('create/', views.TeamApiView.as_view()),
    path('update/<int:id_team>', views.TeamApiView.as_view()),
    path('delete/<int:id_team>', views.TeamApiView.as_view()),
    
    
    
]
