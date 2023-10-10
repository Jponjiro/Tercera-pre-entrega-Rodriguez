from django.urls import path
from Appcoder import views
from .views import formulario_insertar, buscar

urlpatterns = [
    
    path('insertar/', views.formulario_insertar, name='insertar'),
    path('buscar/', views.buscar, name='buscar'),
]
