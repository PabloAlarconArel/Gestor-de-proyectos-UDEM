"""Gestion_De_Proyectos_UDEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from core.urls import core_urlpatterns
from escuela.urls import escuela_urlpatterns
from escuela import views as v



urlpatterns = [
    path('',v.escuela_main,name='escuela_main'),
    path('escuela/', include(escuela_urlpatterns)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls'))
    
 

]

admin.site.site_header = 'Administrador Gestion De Proyectos UDEM'
admin.site.site_title = 'GestionDeProyectosUDEM'    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
