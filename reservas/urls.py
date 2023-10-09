"""
URL configuration for reservas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema.views import reserva_remover, reserva_criar, reserva_listar, detalhe, index, reserva_filtrar

urlpatterns = [
    path("admin/", admin.site.urls),
    path ('',reserva_listar, name='reserva_listar'),
    path ('reserva/remover/<int:id>/',reserva_remover, name='reserva_remover'),
    path('detalhe/<int:id>', detalhe, name= 'detalhe'),
    path ('reserva/criar/',reserva_criar, name='reserva_criar'),
    path('index', index, name='index'),
    path ('reserva/filtrar/',reserva_filtrar, name='reserva_filtrar'),


]   
