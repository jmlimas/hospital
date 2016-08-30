# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,render_to_response,HttpResponseRedirect
from django.template import RequestContext
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from .models import User
from .functions import LogIn
from django.contrib.auth.forms import AuthenticationForm 
 


def inicio(request):
	if request.user.is_authenticated():
		return render_to_response('principal/index.html', context_instance=RequestContext(request))
		
	else:
	    if request.method == 'POST':
	    	formulario = AuthenticationForm()
	    	print formulario
	    	if formulario.is_valid:
		        usuario = request.POST['username']
		        clave = request.POST['password']
		        acceso = authenticate(username=usuario, password=clave)
		        if acceso is not None:
		        	if acceso.is_active:
		        		login(request, acceso)
		        		return HttpResponseRedirect('/')
		        	else:
		        		return render_to_response('noactivo.html', context_instance=RequestContext(request))
		        else:
		        	return render_to_response('nousuario.html', context_instance=RequestContext(request))
	    else:
	        formulario = AuthenticationForm()
	    return render_to_response('principal/login.html',{'formulario':formulario}, context_instance=RequestContext(request))


def userlogin(request):
	if request.method == "POST":
		if 'register_form' in request.POST:
			user_register = UserRegisterForm(request.POST)
			if user_register.is_valid():
				User.objects.create_user(username = user_register.cleaned_data['username'],
				 email = user_register.cleaned_data['email'], 
				 password = user_register.cleaned_data['password'])
				LogIn(request, user_register.cleaned_data['username'],
						user_register.cleaned_data['password'])
				return redirect('/')
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				LogIn(request, login_form.cleaned_data['username'],
						login_form.cleaned_data['password'])
				return redirect('/')
	else:
		user_register = UserRegisterForm()
		login_form = LoginForm()
	return render(request, 'users/login.html', 
				{'user_register' : user_register, 'login_form' : login_form})


def LogOut(request):
	logout(request)
	return redirect('/')



