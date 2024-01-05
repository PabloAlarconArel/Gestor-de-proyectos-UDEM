from django.urls import re_path as url
from django.urls import path 
from core import views 

core_urlpatterns = [
    path('', views.home, name='home'),    
    path('check_profile', views.check_profile, name='check_profile'),           

    path('bodega_dashboard/',views.bodega_dashboard,name="bodega_dashboard"),
    path('colaboradores_dashboard/',views.colaboradores_dashboard,name="colaboradores_dashboard"),
    path('ventas_dashboard/',views.ventas_dashboard,name="ventas_dashboard"),
    ]
