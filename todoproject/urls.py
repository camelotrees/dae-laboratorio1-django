from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('operaciones.urls')),
    path('', include('tasks.urls')),
]