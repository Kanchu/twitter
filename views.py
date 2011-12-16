from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return render_to_response ('home.html',RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
