from django.shortcuts import render

from app.models import *

from django.http import HttpResponse
# Create your views here.


def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('topic is inserted successfully')
    return render(request,'insert_topic.html')

def  insert_webpage(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=='POST':
        topic=request.POST.get('topic')
        na=request.POST['na']
        ur=request.POST.get('ur')
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('Webpage is created')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    QST=Topic.objects.all()       
    d={'topics':QST}

    if request.method=='POST':
        tn=request.POST.get('topic')
        na=request.POST['name']
        u=request.POST['url']
        dt=request.POST['date']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=u)[0]
        W.save()
        A=AccessRecord.objects.get_or_create(name=W,date=dt)[0]
        A.save()
        return HttpResponse('access records inserted successfully')
    return render(request,'insert_access.html',d)