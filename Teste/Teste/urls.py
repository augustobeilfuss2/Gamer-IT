from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # URL padrão
    path('', include('app.urls', namespace='app')),

    # Interface administrativa
    path('admin/', admin.site.urls),
]