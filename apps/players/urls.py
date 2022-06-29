from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.PlayerApiView.as_view()),
    path('detail/<int:id>', views.PlayerDetailView.as_view()),
    path('create/', views.PlayerApiView.as_view()),
    path('update/<int:id>', views.PlayerApiView.as_view()),
    path('delete/<int:id>', views.PlayerApiView.as_view()),
    
]
