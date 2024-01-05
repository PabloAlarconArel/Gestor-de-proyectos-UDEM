from django.shortcuts import render
from django.conf import settings 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group, User 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from django.db.models import Avg, Count, Q 
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect)
from django.shortcuts import redirect, render 
from django.template import RequestContext 
from django.views.decorators.csrf import csrf_exempt 

from users.models import Rol

# Create your views here.
def home(request):
    return redirect('login')

@login_required
def pre_check_profile(request):
    
    pass

@login_required
def check_profile(request):  
    try:
        profile = Rol.objects.filter(user_id=request.user.id).get()    
    except:
        messages.add_message(request, messages.INFO, 'Hubo un error con su usuario, por favor contactese con los administradores')              
        return redirect('login')
    if profile.id== 1:        
        return redirect('/admin/')
    else:
        return redirect('logout')

@login_required
def bodega_dashboard(request):
    profile = Rol.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'core/bodega_dashboard.html'
    return render(request,template_name,{'profile':profile})    

@login_required
def colaboradores_dashboard(request):
    profile = Rol.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'core/colaboradores_dashboard.html'
    return render(request,template_name,{'profile':profile})   

@login_required
def ventas_dashboard(request):
    profile = Rol.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'core/ventas_dashboard.html'
    return render(request,template_name,{'profile':profile})   