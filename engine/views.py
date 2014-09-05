from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from mainapp.models import news, comment, userinfo, baseinfo, project, projectmember
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth import authenticate, login
import datetime

def home(request):
    context = {}
    now = datetime.datetime.now()
    context['curtime'] = now
    context['newssection'] = True
    if request.user.is_authenticated():
        user = userinfo.objects.get(owner = request.user.id)
        context['user'] = user

        basestats = baseinfo.objects.all().filter(show = True).order_by('-name').order_by('-importance')
        context['basestats'] = basestats

        newslist = news.objects.all().order_by('-creationdate')
        paginator = Paginator(newslist, 20)
        newslist = paginator.page(1).object_list
#        page = request.GET.get('page')
#        try:
#                q_list = paginator.page(page)
#        except PageNotAnInteger:
#                q_list = paginator.page(1)
#        except EmptyPage:
#                q_list = paginator.page(paginator.num_pages)
#
        newslist = paginator.page(1)
        context['n_list'] = newslist
        return render_to_response('News.html', context)
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
#                    context['curusername'] = request.user.username
#                    context['loginsuccess'] = True
#                    return render_to_response('News.html', context)
                    return HttpResponseRedirect('/')
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

def profile(request, username_id):
    if request.user.is_authenticated():
        context = {}

        context['peoplesection'] = True

        user = userinfo.objects.get(owner = request.user.id)
        context['user'] = user

        profile = userinfo.objects.get(owner = username_id)
        context['profile'] = profile

        if user == profile:
            context['self'] = True
        else:
            context['self'] = False

        if user.medic == True:
            context['showhealth'] = True
        else:
            context['showhealth'] = False


        now = datetime.datetime.now()
        context['curtime'] = now

        basestats = baseinfo.objects.all().filter(show = True).order_by('-name').order_by('-importance')
        context['basestats'] = basestats

        projectmembers = projectmember.objects.all().filter(owner = profile).order_by('-importance')
        context['projectmembers'] = projectmembers


        return render_to_response('Profile.html', context)
    else:
        return HttpResponseRedirect('/')

def people(request):
    if request.user.is_authenticated():
        context = {}

        user = userinfo.objects.get(owner = request.user.id)
        context['user'] = user

        context['peoplesection'] = True



        people1 = userinfo.objects.all().filter(workssection = "Science section").order_by('-access')
        context['sciencepeople'] = people1

        people2 = userinfo.objects.all().filter(workssection = "Supples section").order_by('-access')
        context['supplespeople'] = people2

        people3 = userinfo.objects.all().filter(workssection = "Medicine section").order_by('-access')
        context['medicinepeople'] = people3

        people4 = userinfo.objects.all().filter(workssection = "Police section").order_by('-access')
        context['policepeople'] = people4




        now = datetime.datetime.now()
        context['curtime'] = now

        basestats = baseinfo.objects.all().filter(show = True).order_by('-name').order_by('-importance')
        context['basestats'] = basestats

        return render_to_response('People.html', context)
    else:
        return HttpResponseRedirect('/')

def projectPage(request, project_id):
    if request.user.is_authenticated():
        context = {}

        context['projectsection'] = True

        user = userinfo.objects.get(owner = request.user.id)
        context['user'] = user

        curproject = project.objects.get(pk = project_id)
        context['project'] = curproject

        now = datetime.datetime.now()
        context['curtime'] = now

        basestats = baseinfo.objects.all().filter(show = True).order_by('-name').order_by('-importance')
        context['basestats'] = basestats


        projectmembers = projectmember.objects.all().filter(project = project_id).order_by('-importance')
        context['projectmembers'] = projectmembers

        return render_to_response('Project.html', context)
    else:
        return HttpResponseRedirect('/')

def projects(request):
    if request.user.is_authenticated():
        context = {}

        context['projectsection'] = True

        user = userinfo.objects.get(owner = request.user.id)
        context['user'] = user

        now = datetime.datetime.now()
        context['curtime'] = now

        basestats = baseinfo.objects.all().filter(show = True).order_by('-name').order_by('-importance')
        context['basestats'] = basestats

        projects = project.objects.all().filter(show = True).order_by('-name').order_by('-rating')
        paginator = Paginator(projects, 20)
        projects = paginator.page(1).object_list
        newslist = paginator.page(1)
        context['p_list'] = projects
        return render_to_response('Projects.html', context)
    else:
        return HttpResponseRedirect('/')
    

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return HttpResponseRedirect('/')
    else:
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
