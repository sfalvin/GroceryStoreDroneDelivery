# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def hiSaajan(request):
    return HttpResponse("Hello saajan")

def tracking_home(request):
    # render simple static page
    template = loader.get_template('home/tracking_home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def tracking(request):
	# render simple static page
    template = loader.get_template('home/tracking.html')
    context = {}
    return HttpResponse(template.render(context, request))

# Create your views here.
