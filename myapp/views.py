from django.shortcuts import render, redirect
from django.contrib import messages
from myapp.models import Contact, Donate
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        feedback = request.POST.get('feedback')
        
        contact = Contact(name=name, email=email, phone=phone, age=age, feedback=feedback, date=datetime.today())
        contact.save()
        messages.success(request, 'Your contact information has been submitted successfully.')
        return redirect('contact')  # Redirect to the same view to clear the form
    return render(request, 'contact.html')

def donate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        donation = request.POST.get('donation')
        
        donate = Donate(name=name, email=email, password=password, phone=phone, address=address, donation=donation, date=datetime.today())
        donate.save()
        messages.success(request, 'Donation successfully recorded.')
        return redirect('donate')  # Redirect to the same view to clear the form
    return render(request, 'donate.html')
