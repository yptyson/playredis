from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
import redis


def new(request):
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def edit(request):
    r = redis.Redis()
    company_name = request.GET.get('name')
    return render_to_response('company/edit.html',{'company':r.hgetall(company_name)},context_instance=RequestContext(request))

def update(request):
    r = redis.Redis()
    name = request.POST.get('name')
    r.hset(name,'num',request.POST.get('num'))
    r.hset(name,'desc',request.POST.get('desc'))
    return render_to_response('company/details.html',{'company':r.hgetall(name)})

def show(request):
    r = redis.Redis()
    return render_to_response('company/show.html',{'companys':r.lrange('companys',0,-1)})

def details(request):
    r = redis.Redis()
    company_name = request.GET.get('name')
    return render_to_response('company/details.html',{'company':r.hgetall(company_name)})

def save(request):
    r = redis.Redis()
    r.hset(name,'name',request.POST.get('name'))
    r.hset(name,'desc',request.POST.get('desc'))
    r.hset(name,'num',request.POST.get('num'))
    r.lpush('companys',name)

    return redirect("/company/show/")