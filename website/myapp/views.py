from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact


def index(request):

    return render(request, 'index.html')
    #return HttpResponse("Hello Index page")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if(request.method=='POST'):
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name= name,  email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        message = {'msg':'Form Submitted Succesfully !'}
        return render(request, 'contact.html', message)


    return render(request, 'contact.html')

