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

from models import User2,engine#,session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Session=sessionmaker()
Session.configure(bind=engine)
session=Session()

def play(request):
    ed_user= User(username='tyson3', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    session.commit()

    return  render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def play2(request):
    session.add_all([
        User2(username='tysonb1', fullname='Ed'),
        User2(username='tysonb2', fullname='Ed')
        ])
    print session.dirty
    session.commit()

    return  render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def query_(request):
    print session.query(User2).filter(User2.username.in_(['tysona1','tysona2']))#.all()
    # SELECT users2.id AS users2_id, users2.username AS users2_username, users2.fullname AS users2_fullname
    # FROM users2  WHERE users2.username IN (:username_1, :username_2)
    print session.query(User2).filter(User2.username.in_(['tysona1','tysona2'])).all()
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def query(request):
    for instance in session.query(User2).order_by(User2.id):
        print instance.username, instance.fullname
    for item in  session.query(User2.username.label('name_label')).all():
        print(item.name_label)
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def cut(request):
    for u in session.query(User2).order_by(User2.id)[1:3]:
        print u
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def filter_by(request):
    for name, in session.query(User2.username).filter_by(fullname='Ed Jones'):
        print name
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def filter(request):
    for name, in session.query(User2.username).filter(User2.fullname=='Ed Jones'):
        print name
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def doublefilter(request):
    for user in session.query(User2).filter(User2.username=='tysona1').filter(User2.fullname=='Ed Jones'):
        print user.fullname
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def likefilter(request):
    for item in session.query(User2).filter(User2.username.like('%ty%')):
        print item.username
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def infi(request):
    for item in session.query(User2).filter(User2.username.in_(['tysona1', 'tysona2'])):
        print item.username
    # filter(~User.name.in_(['ed', 'wendy', 'jack']))
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

# query.filter(User.name == None)
# query.filter(User.name != None)

from sqlalchemy import and_
def andf(request):
    for item in session.query(User2).filter(and_(User2.username == 'tysona1', User2.fullname == 'Ed Jones')):
        print item.username
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

from sqlalchemy import or_
def orf(request):
    for item in session.query(User2).filter(or_(User2.username=='tysona1',User2.username=="tysona2")):
        print item.username
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

from sqlalchemy.orm.exc import MultipleResultsFound
def orlist(request):
    #all(),first(),one()
    try:
        user = session.query(User2).filter(User2.username=="tysona1").one()
        print user
    except MultipleResultsFound, e:
        print e
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def para(request):
    for item in session.query(User2).filter("id<:value and username=:name").params(value=224, name='tysona1').order_by(User2.id):
        print item.username
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))


def psql(request):
    for item in session.query(User2).from_statement("SELECT * FROM users2 where username=:name").params(name='tysona1').all():
        print item.username
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))

def ql(request):
    for id,username in session.query("id", "username").from_statement("SELECT * FROM users2 where username=:name").params(name='tysona1').all():
        print id,'---',username
    return render_to_response('company/new.html',{'name':'yuanpeng'},context_instance=RequestContext(request))








