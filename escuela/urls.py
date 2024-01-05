from django.urls import path
from escuela import views 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


escuela_urlpatterns = [
    path('escuela_add_rest/', views.escuela_add_rest),
    path('escuela_update_element_rest/', views.escuela_update_element_rest),
    path('escuela_list_rest/', views.escuela_list_rest),
    path('escuela_bloqueado/', views.escuela_bloqueado),
    path('escuela_list_contains/', views.escuela_list_contains),
    
    path('escuela_main/', views.escuela_main, name="escuela_main"),
    path('escuela_add/', views.escuela_add, name="escuela_add"),
    path('escuela_list/', views.escuela_list, name="escuela_list"),
    path('escuela_filter/', views.escuela_filter, name="escuela_filter"),
    path('escuela_ver/<escuela_id>/', views.escuela_ver, name="escuela_ver"),

    path('escuela_save/', views.escuela_save, name="escuela_save"),
    path('escuela_update/', views.escuela_update, name="escuela_update"),
    path('escuela_bloquear/<escuela_id>/', views.escuela_bloquear, name="escuela_bloquear"),
    ]