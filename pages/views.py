# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Page
from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
	return render_to_response('default.html', {})
