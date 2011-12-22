# Create your views here.
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from registeruser.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.conf import settings as django_settings

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')

    else:
        form = RegistrationForm()
        variables = RequestContext(request, {
                'form': form
            })
        return render_to_response('registration/register.html',variables)

def custom_login(request, template_name, authentication_form):
    template_name = template_name
    if request.user.is_authenticated():
        return HttpResponseRedirect(django_settings.LOGIN_REDIRECT_URL)
    else:
        return login(request, template_name=template_name, authentication_form=authentication_form)
