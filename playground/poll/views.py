from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from poll.models import Person
from django.views.decorators.csrf import csrf_exempt


def home(request):
    template=loader.get_template('home.html')

    return HttpResponse(template.render())



def persons(request):
 
    template=loader.get_template('persons.html')
    p=Person.objects.all()
    context={
      'p':p
    }

    return HttpResponse(template.render(context,request))

def pdetails(request,id):
 
    template=loader.get_template('pdetails.html')
    p=Person.objects.get(id=id)
    context={
      'p':p
    }

    return HttpResponse(template.render(context,request))


def delete(request,id):
 
    template=loader.get_template('deletesuccess.html')
    p=Person.objects.get(id=id)
    p.delete()
    # context={
    #   'p':p
    # }

    return HttpResponse(template.render())


def addpage(request):
 
    template=loader.get_template('addpage.html')

    

    return HttpResponse(template.render())

@csrf_exempt
def create(request):

    template=loader.get_template('addsuccess.html')
    context={

    }
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        city=request.POST['city']
        dob=request.POST['dob']
        print(name,age,city,dob)
        p=Person(name=name,age=age,city=city,dob=dob)
        p.save()

    return HttpResponse(template.render(context,request))


def updatepage(request,id):
 
    template=loader.get_template('updatepage.html')
    p=Person.objects.get(id=id)
    context={
            'p':p
    }

    

    return HttpResponse(template.render(context,request))

@csrf_exempt
def update(request,id):

    template=loader.get_template('updatesuccess.html')

    
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        city=request.POST['city']
        dob=request.POST['dob']
        p=Person.objects.get(id=id)
        p.name=name
        p.age=age
        p.city=city
        p.dob=dob
        p.save()
        context={
            'p':p
    }

    return HttpResponse(template.render(context,request))