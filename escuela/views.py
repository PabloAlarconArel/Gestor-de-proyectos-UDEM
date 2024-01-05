from genericpath import exists
import json

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from users.models import Rol

from rest_framework import generics, viewsets
from rest_framework.decorators import (
	api_view, authentication_classes, permission_classes)
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from escuela.models import Escuela
from django.db.models import Count, Avg, Q

# Create your views here.


#templates
@login_required
def escuela_main(request):
    profile = Rol.objects.get(id=request.user.id)
    if profile.id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'escuela/escuela_main.html'
    return render(request,template_name,{'profile':profile})

@login_required
def escuela_add(request):
    profile = Rol.objects.get(id=request.user.id)
    if profile.id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'escuela/escuela_add.html'
    return render(request,template_name,{'profile':profile})


@login_required
def escuela_list (request,page=None,search=None):
    profile = Rol.objects.get(id=request.user.id)
    if profile.id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if page == None:
        page = request.GET.get('page')
    else:
        page = page
    if request.GET.get('page') == None:
        page = page
    else:
        page = request.GET.get('page') 
    if search == None:
        search = request.GET.get('search')
    else:
        search = search
    if request.GET.get('search') == None:
        search = search
    else:
        search = request.GET.get('search') 
    if request.method == 'POST':
        search = request.POST.get('search') 
        page = None
    h_list = []
    if search == None or search == "None":
        h_count = Escuela.objects.count()
        h_list_array = Escuela.objects.order_by('nombre').filter(estado="Activado")
        for h in h_list_array:
            h_list.append({'id':h.id,'nombre':h.nombre,'direccion':h.direccion, 'correo':h.correo, 'telefono' :h.telefono,'estado' :h.estado})
    else:
        h_count = Escuela.objects.filter(nombre__icontains=search).count()
        h_list_array = Escuela.objects.filter(nombre__icontains=search).order_by('id')
        for h in h_list_array:
            h_list.append({'id':h.id,'nombre':h.nombre,'direccion':h.direccion, 'correo':h.correo, 'telefono' :h.telefono,'estado' :h.estado})         
    paginator = Paginator(h_list, 5) 
    h_list_paginate= paginator.get_page(page)   
    template_name = 'escuela/escuela_list.html'
    return render(request,template_name,{'template_name':template_name,'h_list_paginate':h_list_paginate,'paginator':paginator,'page':page})

@login_required
def escuela_filter (request,page=None,search=None):
    profile = Rol.objects.get(id=request.user.id)
    if profile.id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if page == None:
        page = request.GET.get('page')
    else:
        page = page
    if request.GET.get('page') == None:
        page = page
    else:
        page = request.GET.get('page') 
    if search == None:
        search = request.GET.get('search')
    else:
        search = search
    if request.GET.get('search') == None:
        search = search
    else:
        search = request.GET.get('search') 
    if request.method == 'POST':
        search = request.POST.get('search') 
        page = None
    h_list = []
    if search == None or search == "None":
        h_count = Escuela.objects.count()
        h_list_array = Escuela.objects.order_by('nombre').filter(estado="bloqueado")
        for h in h_list_array:
            h_list.append({'id':h.id,'nombre':h.nombre,'direccion':h.direccion, 'correo':h.correo, 'telefono' :h.telefono,'estado' :h.estado})
    else:
        h_count = Escuela.objects.filter(nombre__icontains=search).count()
        h_list_array = Escuela.objects.filter(nombre__icontains=search).order_by('id')
        for h in h_list_array:
            h_list.append({'id':h.id,'nombre':h.nombre,'direccion':h.direccion, 'correo':h.correo, 'telefono' :h.telefono,'estado' :h.estado})         
    paginator = Paginator(h_list, 5) 
    h_list_paginate= paginator.get_page(page)   
    template_name = 'escuela/escuela_filter.html'
    return render(request,template_name,{'template_name':template_name,'h_list_paginate':h_list_paginate,'paginator':paginator,'page':page})

@login_required
def escuela_ver(request,escuela_id):
    profile = Rol.objects.get(id=request.user.id)
    if profile.id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    escuela_data = Escuela.objects.get(pk=escuela_id)
    template_name = 'escuela/escuela_ver.html'
    return render(request,template_name,{'profile':profile,'escuela_data':escuela_data})

@login_required
def escuela_save(request):
    profile = Rol.objects.get(id=request.user.id)
    if profile.id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        correo = request.POST['correo'] 
        telefono = request.POST['telefono']                     
        escuela_save = Escuela(
            nombre = nombre,
            direccion = direccion,
            correo = correo,
            telefono = telefono,
            )
        escuela_save.save()
        messages.add_message(request, messages.INFO, 'Escuela ingresada con éxito')
        return redirect('escuela_list')
    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')

@login_required
def escuela_update(request):
    profile = Rol.objects.get(user_id=request.user.id)
    if profile.user_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        escuela_id=request.POST['id']
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        correo = request.POST['correo'] 
        telefono = request.POST['telefono']


        Escuela.objects.filter(pk = escuela_id).update(nombre = nombre)
        Escuela.objects.filter(pk = escuela_id).update(direccion = direccion)
        Escuela.objects.filter(pk = escuela_id).update(correo = correo)
        Escuela.objects.filter(pk = escuela_id).update(telefono = telefono)
        messages.add_message(request, messages.INFO, 'Escuela ingresada con éxito')
        return redirect('escuela_list')
    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')


@login_required
def escuela_bloquear(request,escuela_id):
    
    profile = Rol.objects.get(user_id=request.user.id)
    if profile.Rol_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    escuela_array=Escuela.objects.get(pk=escuela_id) 
    if escuela_array.estado == "Activado":
        estado="bloqueado"
        Escuela.objects.filter(pk=escuela_id).update(estado=estado)
        messages.add_message(request, messages.INFO, 'Escuela desactivada')
        return redirect('escuela_list')
    if escuela_array.estado == "bloqueado":
        messages.add_message(request, messages.INFO, 'Escuela ya esta bloqueada')
        return redirect('escuela_list')
    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')



#          #CAMBIAR ESTADO
#   def departamento_cambio_estado(request,id):
#          departamento= get_object_or_404(Departamento,id=id)
#          Departamento.objects.filter(id=id).update(estado="bloqueado")
#          return redirect('aplication:main')



#-------------------------------endpoint-------------------------------------------------------------
@api_view(['POST'])
def escuela_add_rest(request, format=None):    
    if request.method == 'POST':
        nombre = request.data['nombre']
        direccion = request.data['direccion']
        correo = request.data['correo'] 
        telefono = request.data['telefono']
        
        if isinstance(nombre,int):
            return Response({'Msj': "Error los datos son invalidos"})
        if isinstance(direccion,int):
            return Response({'Msj': "Error los datos son invalidos"})
        if isinstance(correo,int):
            return Response({'Msj': "Error los datos son invalidos"})
        if isinstance(telefono,int):
            return Response({'Msj': "Error los datos son invalidos"})
        if nombre.isspace() or direccion.isspace() or correo.isspace() or telefono.isspace():
            return Response({'Msj': "Error los datos no pueden ser espacios"})
        if nombre.isdigit() or correo.isdigit() :
            return Response({'Msj': "el nombre o correo no puede ser numeros"})
        if telefono.isalpha()  :
            return Response({'Msj': "el telefono no puede ser letras"})    
        if nombre == '' or direccion == '' or correo == '' or telefono  =='':
            return Response({'Msj': "Error los datos no pueder estar en blanco"})                         
        escuela_save = Escuela(
            nombre = nombre,
            direccion = direccion,
            correo = correo,
            telefono = telefono,
            )
        escuela_save.save()
        return Response({'Msj': "Escuela creada exitosamente"})
    else:
        return Response({'Msj': "Error método no soportado"}) 


@api_view(['POST'])
def escuela_update_element_rest(request, format=None):
    if request.method == 'POST':
        try:
            escuela_id = request.data['escuela_id']
            if isinstance(escuela_id,float):
                return Response({'Msj': "El ID debe ser numerico entero"})
            if isinstance(escuela_id,str):
                return Response({'Msj': "El ID debe ser numerico entero"})
            escuela_array = Escuela.objects.get(pk = escuela_id)
            nombre = request.data['nombre']
            direccion = request.data['direccion']
            correo = request.data['correo']
            telefono = request.data['telefono']
            if not isinstance(nombre,str):
                return Response({'Msj': "Error los datos son invalidos"})
            if not isinstance(direccion,str):
                return Response({'Msj': "Error los datos son invalidos"})
            if not isinstance(correo,str):
                return Response({'Msj': "Error los datos son invalidos"})
            if not isinstance(telefono,str):
                return Response({'Msj': "Error los datos son invalidos"})
            if nombre.isspace() or direccion.isspace() or correo.isspace() or telefono.isspace():
                return Response({'Msj': "Error los datos no pueden ser espacios"})
            if nombre.isdigit() or correo.isdigit() :
                return Response({'Msj': "el nombre o correo no puede ser numeros"})
            if telefono.isalpha()  :
                return Response({'Msj': "el telefono no puede ser letras"})    
            if nombre == '' or direccion == '' or correo == '' or telefono  =='':
                return Response({'Msj': "Error los datos no pueder estar en blanco"})  
            if escuela_array:
                Escuela.objects.filter(pk = escuela_id).update(nombre = nombre)
                Escuela.objects.filter(pk = escuela_id).update(direccion = direccion)
                Escuela.objects.filter(pk = escuela_id).update(correo = correo)
                Escuela.objects.filter(pk = escuela_id).update(telefono = telefono)
                return Response({'Msj' : 'Escuela editada con éxito'})
        except Escuela.DoesNotExist:
            return Response({'Msj' : 'No existe Escuela para editar'})
        except ValueError:
            return Response({'Msj':"Valor no soportado"})    
    else:
        return Response({'Msj' : 'Error método no soportado'})

@api_view(['GET'])
def escuela_list_rest(request, format=None):    
    if request.method == 'GET':
        try:
            escuela_list =  Escuela.objects.filter(estado = "Activado")
            escuela_json = []
            for s in escuela_list:
                escuela_json.append({'Escuela':s.nombre,'direccion': s.direccion,'correo':s.correo,'telefono':s.telefono})
            return Response({'Listado': escuela_json})
        except Escuela.DoesNotExist:
            return Response({'Msj' : 'No existe sucursal para listar'})
    else:
        return Response({'Msj': "Error método no soportado"})

@api_view(['POST'])
def escuela_bloqueado(request, format=None):
    if request.method == 'POST':
        try:
            escuela_id = request.data['escuela_id']
            
            if not isinstance(escuela_id,int):
                return Response({'Msj': "Error los datos son invalidos"})
            escuela_lista =  Escuela.objects.get(pk=escuela_id)
            if escuela_lista == False :
                return Response({'Msj': "no existe Escuela"})
            lista_desactivados=  Escuela.objects.get (pk=escuela_id , estado ="desactivado")
            if lista_desactivados == True :
                return Response({'Msj': "Escuela ya se encuentra bloqueada"})

            Escuela.objects.get(pk=escuela_id).update(estado="desactivado")
            return Response({"Msj": "Escuela bloqueada correctamente"})
        except Escuela.DoesNotExist:
            return Response({'Msj' : 'No existe Escuela para bloquear'})
    else:
        return Response({"Msj": "Error en método, se debe usar método POST"})


@api_view(['POST'])
def escuela_list_contains(request, format=None):
    if request.method == 'POST':
        search = request.data['search']
        escuela_list_count=Escuela.objects.filter(Q(nombre__icontains=search)).count()
        if escuela_list_count > 0:
            escuela_list = Escuela.objects.filter(Q(nombre__icontains=search)).order_by('nombre')
            escuela_json = []
            for h in escuela_list:
                escuela_json.append({'nombre':h.nombre,'direccion': h.direccion,'correo':h.correo,'telefono':h.telefono})
            return Response({'Listado':escuela_json})
        else:
            return Response({'Msj':'No existen Escuelas en estado o nombre con la cadena'})    
    else:
        return Response({'Msj':'Error método no soportado'}) 

          