from django.shortcuts import render
from .models import Contact

def home(request):
    return render(request, 'scoop_app/home.html')

def about(request):
    return render(request, 'scoop_app/about.html')

def products(request):
    return render(request, 'scoop_app/products.html')

def contact(request):
    success = False
    error = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            success = True
        else:
            error = True
    return render(request, 'scoop_app/contact.html',{
        'success' : success,
        'error' : error
    })
        
    
