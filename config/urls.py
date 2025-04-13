from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter



schema_view = get_schema_view(
    openapi.Info(
        title="Sizning API'yingiz nomi",
        default_version='v1',
        description="API hujjati",
        contact=openapi.Contact(email="aloqa@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_app.urls')),  # bu sizning app'ga yo‘l

    # Swagger yo‘llari
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
