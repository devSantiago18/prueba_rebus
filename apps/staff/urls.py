from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.StaffApiView.as_view()),
    path('detail/<int:id_team>', views.StaffDetailView.as_view()),
    path('create/', views.StaffApiView.as_view()),
    path('update/<int:id_team>', views.StaffApiView.as_view()),
    path('delete/<int:id_team>', views.StaffApiView.as_view()),
]
