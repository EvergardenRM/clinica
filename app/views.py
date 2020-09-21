from django.shortcuts import render
from django.shortcuts import render,  HttpResponse
from django.http import  HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render,  HttpResponse, redirect, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from app.forms import * 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy 
from app.models import * 


def plantilla(request):
    return render(request, 'plantilla.html')


def crear_especialidad(request , base ='crear_especialidad.html'):
    if request.method == 'POST':
        formulario = EspecialidadForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('plantilla')
    else:
        formulario =EspecialidadForm()
    return render(request, base, {'forms': formulario})

def crear_cliente(request, base = 'crear_cliente.html'):
    if request.method == 'POST':
        formulario =ClienteForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('plantilla')
    else:
        formulario = ClienteForm
    return render(request, base ,{'forms': formulario})

def crear_medico(request , base = 'crear_cliente.html'):
    if request.method == 'POST':
        formulario = medicoForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('plantilla')
    else:
        formulario= medicoForm()
    return render(request, base, {'forms': formulario })

def crear_cita(request, base = 'crear_cita.html'):
    if request.method == 'POST':
        formulario = citaForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('plantilla')
    else:
        formulario = citaForm()
    return render(request, base, {'forms': formulario})


def modificar_especialidad(request,pk, base = 'modificar_especialidad.html'):
    if request.method =='POST':
        datos = get_object_or_404(Especializacion,pk=pk)
        formulario = EspecialidadForm(request.POST or None, instance = datos)
        if formulario.is_valid():
            formulario.save()
            return redirect("plantilla")
    else: 
        datos = get_object_or_404(Especializacion, pk=pk)
        formulario = EspecialidadForm(request.POST or None,  instance = datos)
    return render(request,base, {'forms':formulario})

def modificar_cliente(request,pk,base = 'modificar_cliente.html'):
    if request.method =='POST':
        estado = cliente.objects.get(pk=pk)
        estado.estado = 0
        datos = get_object_or_404(cliente,pk=pk)
        formulario = ClienteForm(request.POST or None, instance = datos)
        if formulario.is_valid():
            estado.save()
            return redirect("plantilla")
    else: 
        datos = get_object_or_404(Especializacion, pk=pk)
        formulario = ClienteForm(request.POST or None,  instance = datos)
    return render(request,plantilla, {'forms':formulario})


def modificar_medico(request,pk,base = 'modificar_medico.html'):
    if request.method =='POST':
        estado = medico.objects.get(pk=pk)
        estado.estado = 0
        datos = get_object_or_404(medico,pk=pk)
        formulario = medicoForm(request.POST or None, instance = datos)
        if formulario.is_valid():
            estado.save()
            return redirect("plantilla")
    else: 
        datos = get_object_or_404(medico, pk=pk)
        formulario = medicoForm(request.POST or None,  instance = datos)
    return render(request,plantilla, {'forms':formulario})

def modificar_cita(request ,pk,base = 'modificar_cita.html'):
    if request.method =='POST':
        estado = cita.objects.get(pk=pk)
        estado.estado = 0
        datos = get_object_or_404(cita,pk=pk)
        formulario = citaForm(request.POST or None, instance = datos)
        if formulario.is_valid():
            estado.save()
            return redirect("plantilla")
    else: 
        datos = get_object_or_404(cita, pk=pk)
        formulario = citaForm(request.POST or None,  instance = datos)
    return render(request,plantilla, {'forms':formulario})

def vista_especialidad(request, base = 'vista_especialidad.html'):
    datos = Especializacion.objects.filter(estado = 1)
    return render(request, base, {'datos': datos})
    
def eliminar_especialidad(request, pk, base="eliminar_especialidad.html"):
    if request.method == "POST":
        estado = Especializacion.objects.get(pk=pk)
        estado.estado = 0 
        datos = get_object_or_404(Especializacion, pk=pk)
        formulario = EspecialidadForm(request.POST or None, instance=datos)    
        if formulario.is_valid():             
            estado.save()
            print(estado.id)
            return redirect("plantilla")
    else:
        datos = get_object_or_404(Especializacion, pk=pk)
        formulario = EspecialidadForm(request.POST or None, instance=datos)
    return render(request, base, {'forms': formulario})

def eliminar_medico(request, pk, plantilla="elimitar_medico.html"):
    if request.method == "POST":
        estado = medico.objects.get(pk=pk)
        estado.estado = 0 
        datos = get_object_or_404(medico, pk=pk)
        formulario= medicoForm(request.POST or None, instance=datos)    
        if formulario.is_valid():             
            estado.save()
            print(estado.id)
            return redirect("plantilla")
    else:
        datos = get_object_or_404(medico, pk=pk)
        formulario = medicoForm(request.POST or None, instance=datos)
    return render(request, plantilla, {'forms': formulario})

def eliminar_cita(request, pk, base="elimitar_citas.html"):
    if request.method == "POST":
        estado = cita.objects.get(pk=pk)
        estado.estado = 0 
        datos = get_object_or_404(cita, pk=pk)
        formulario= citaForm(request.POST or None, instance=datos)    
        if formulario.is_valid():             
            estado.save()
            print(estado.id)
            return redirect("plantilla")
    else:
        datos = get_object_or_404(cita, pk=pk)
        formulario = citaForm(request.POST or None, instance=datos)
    return render(request,base, {'forms': formulario})

def eliminar_cliente(request, pk, plantilla="elimitar_cliente.html"):
    if request.method == "POST":
        estado = cliente.objects.get(pk=pk)
        estado.estado = 0 
        datos = get_object_or_404(cliente, pk=pk)
        formulario= ClienteForm(request.POST or None, instance=datos)    
        if formulario.is_valid():             
            estado.save()
            print(estado.id)
            return redirect("plantilla")
    else:
        datos = get_object_or_404(cliente, pk=pk)
        formulario = cliente(request.POST or None, instance=datos)
    return render(request, plantilla, {'forms': formulario})






    
