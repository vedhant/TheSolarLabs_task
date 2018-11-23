# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urlparse import parse_qs

from django.shortcuts import render, redirect
from .models import UserDemo
from . import form

# Create your views here.

def showform(request):
	if request.method == "POST":
		demo_form = form.CreateDemoUser(request.POST)
		if demo_form.is_valid():
			demo_form.save()
			return redirect('/')
		else:
			demo_form = form.CreateDemoUser()
			return render(request, 'demo/demo_form.html', {'form': demo_form, 'error': True})
	demo_form = form.CreateDemoUser()
	return render(request, 'demo/demo_form.html', {'form': demo_form, 'error': False})