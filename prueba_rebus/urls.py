from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('teams/', include('apps.teams.urls')),
    re_path('players/', include('apps.players.urls')),
    re_path('staff/', include('apps.staff.urls')),
    re_path('resumen/', include('apps.resumen.urls')),
]
