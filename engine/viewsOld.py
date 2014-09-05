from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.contrib import auth

def home(request, str1 = 'anonim'):
    context = {'anonim': True}
    context.update(csrf(request))
    return render_to_response('News.html', context)
