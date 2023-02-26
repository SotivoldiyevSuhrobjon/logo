from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    about = About.objects.all().first()
    service = Service.objects.all()
    client = Clien.objects.all()
    service_count = service.count()
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        make=Make.objects.create(
            name=name, email=email, message=message,
        ) 
        make.save()
    context={
        'service_count':service_count,
        'about': about,
        'service' : service,
        'client' : client,

    }
    return render(request, 'main.html', context)