from django.shortcuts import render
from django.shortcuts import render,  HttpResponse
from django.http import  HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render,  HttpResponse, redirect, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from  django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy 


def plantilla(request):
    return render(request, 'plantilla.html')

