"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.plantilla, name='plantilla' ),
    path('crear_especialidad/',views.crear_especialidad, name='crear_especialidad'),
    path('crear_cliente/',views.crear_cliente, name='crear_cliente'),
    path('crear_medico/',views.crear_medico, name='crear_medico'),
    path('crear_cita/',views.crear_cita, name='crear_cita'),
    path('modificar_especialidad/<int:pk>',views.modificar_especialidad, name='modificar_especialidad'),
    path('modificar_medico/<int:pk>',views.modificar_medico, name='modificar_medico'),
    path('modificar_cita/<int:pk>',views.modificar_cita, name='modificar_cita'),
    path('modificar_cliente/<int:pk>',views.modificar_cliente, name='modificar_cliente'),
    path('vista_especialidad/',views.vista_especialidad, name='vista_especialidad'),

]
