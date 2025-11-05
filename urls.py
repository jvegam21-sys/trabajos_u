from django.contrib import admin
from django.urls import path
from estudiantes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registrar_estudiante, name='registrar'),
    path('exito/', views.exito, name='exito'),
]
