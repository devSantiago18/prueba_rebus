
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ResumenApiView.as_view())    
]