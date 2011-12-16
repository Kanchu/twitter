# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from registeruser.forms import RegistrationForm
from django.http import HttpResponseRedirect

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')
        else:
            form = RegistrationForm()
            variables = RequestContext(request, {
                'form': form
            })
        return render_to_response('registration/register.html',variables)
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {
                'form': form
            })
        return render_to_response('registration/register.html',variables)

