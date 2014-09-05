from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
#from django.contrib import auth
from django.contrib.auth import authenticate, login

def home(request, str1 = 'anonim'):
    context = {}
    if request.user.is_authenticated():
#        context['anonim'] = True
#        context.update(csrf(request))
        context['curusername'] = '123'#request.user.username
        return render_to_response('News.html', context)
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    context['curusername'] = request.user.username
                    context['loginsuccess'] = True
                    return render_to_response('News.html', context)
                else:
                    context['logindisabled'] = True
                    context.update(csrf(request))
                    return render_to_response('NewsExample.html', context)
            else:
                context['loginfault'] = True
                context.update(csrf(request))
                return render_to_response('NewsExample.html', context)
        else:
            context.update(csrf(request))
            return render_to_response('NewsExample.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
#
#
#
#def my_view(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
#    if user is not None:
#        if user.is_active:
#            login(request, user)
#            # Redirect to a success page.
#        else:
#            # Return a 'disabled account' error message
#    else:
#        # Return an 'invalid login' error message.
