from django.contrib import admin
from django.urls import path, re_path, include
# Docs modules
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Fifa API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="santiago.dangond18@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('teams/', include('apps.teams.urls')),
    re_path('players/', include('apps.players.urls')),
    re_path('staff/', include('apps.staff.urls')),
    re_path('resumen/', include('apps.resumen.urls')),
    
    
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
