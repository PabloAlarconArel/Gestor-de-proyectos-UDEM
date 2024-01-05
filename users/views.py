from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from users.models import Rol, user
from users.forms import FormCreateUser,FormUpdateUser, FormBlockUser, FormUnblockUser

"""
Roles ID
1=Admin
2=Rector
3=Director
4=Representante
"""

# Generic ListView
class ListUser(ListView):
    model = user
    template_name = 'list_user.html'

    #Verify user=admin
    def get(self,request):
        profile = self.model.objects.get(id=request.user.id)
        if profile.role_id != 1:
            messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
            return redirect('users:list_blocked_user')
        #Search
        search= request.GET.get('search')
        object_list=self.model.objects.filter(its_active=True).order_by('id')
        if search:
            object_list = self.model.objects.filter(
                Q(names__icontains=search)|
                Q(lastnames__icontains = search)
            ).order_by('id')
        #Pagination
        paginator = Paginator(object_list, 25) # Show 25 users per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,self.template_name,{'page_obj':page_obj})          
        

# Generic ListView to Block Users
class ListBlockUser(ListView):
    model = user
    template_name = 'list_blocked_user.html'

    #Verify user=admin
    def get(self,request):
        profile = self.model.objects.get(id=request.user.id)
        if profile.role_id != 1:
            messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
            return redirect('users:list_blocked_user')
        #Search
        search= request.GET.get('search')
        object_list=self.model.objects.filter(its_active=False).order_by('id')
        if search:
            object_list = self.model.objects.filter(
                Q(names__icontains=search)|
                Q(lastnames__icontains = search)
            ).order_by('id')
        #Pagination
        paginator = Paginator(object_list, 25) # Show 25 users per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,self.template_name,{'page_obj':page_obj})   

# Generic CreateViewView
class CreateUser(CreateView):
    model = user
    template_name = 'create_user.html'
    form_class= FormCreateUser
    success_url = reverse_lazy('users:list_user')

    #Verify user=admin
    def get(self,request,*args, **kwargs):
        profile = user.objects.get(id=request.user.id)
        if profile.role_id != 1:
            messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
            #return redirect('')
        return render(request,self.template_name,{'form': self.form_class})

# Generic UpdateView
class UpdateUser(UpdateView):
    model = user
    form_class= FormUpdateUser
    template_name = 'update_user.html'
    success_url = reverse_lazy('users:list_user')

    #Verify user=admin
    def get(self,request,*args, **kwargs):
        profile = user.objects.get(id=request.user.id)
        if profile.role_id != 1:
            messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
            #return redirect('')
        form = self.form_class(instance=self.get_object())
        return render(request,self.template_name,{'form': form,'object':self.get_object()})    

# Generic BlockUser
class BlockUser(UpdateView):
    model = user
    template_name = 'block_user.html'
    form_class= FormBlockUser
    success_url = reverse_lazy('users:list_user')

    #Verify user=admin
    def get(self,request,*args, **kwargs):
        profile = user.objects.get(id=request.user.id)
        if profile.role_id != 1:
            messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
            #return redirect('')
        form = self.form_class(instance=self.get_object())
        return render(request,self.template_name,{'form': form,'object':self.get_object()})     

# Generic BlockUser
class UnblockUser(UpdateView):
    model = user
    template_name = 'unblock_user.html'
    form_class= FormUnblockUser
    success_url = reverse_lazy('users:list_blocked_user')

    #Verify user=admin
    def get(self,request,*args, **kwargs):
        profile = user.objects.get(id=request.user.id)
        if profile.role_id != 1:
            messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
            #return redirect('')
        form = self.form_class(instance=self.get_object())
        return render(request,self.template_name,{'form': form,'object':self.get_object()})        

class ListRol(ListView):
    model = Rol
    template_name = 'list_rol.html'

    def get(self,request,*args, **kwargs):
        profile = user.objects.get(id=request.user.id)
        if profile.role_id != 1:
            print(profile.role)
            messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
            #return redirect('')
        
        object_list=self.model.objects.filter(its_active=True).order_by('id')

        return render(request,self.template_name,{'object_list':object_list,'paginator':self.paginate_by})

class ListBlockRol(ListView):
    model = Rol
    template_name = 'list_blocked_rol.html'

    def get(self,request,*args, **kwargs):
        profile = user.objects.get(id=request.user.id)
        if profile.role_id != 1:
            print(profile.role)
            messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
            #return redirect('')
        return render(request,self.template_name,{'object_list':self.model.objects.filter(its_active=False).order_by('id')})

class BlockRol(UpdateView):
    model = Rol
    template_name = 'block_rol.html'
    form_class = FormBlockUser
    success_url = reverse_lazy('users:list_rol')

class UnblockRol(UpdateView):
    model = Rol
    template_name = 'unblock_rol.html'
    form_class = FormUnblockUser
    success_url = reverse_lazy('users:list_blocked_rol')
