from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Products


def home(request):
    products = Products.objects.all()[:3]
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Good')
            return redirect('/')
    return render(request, 'index.html', {'products': products, 'form': form})


def contact(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Good')
            return redirect('/')

    return render(request, 'contact.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def chocolate(request):
    products = Products.objects.all()
    return render(request, 'chocolate.html', {'products': products})


def testimonial(request):
    return render(request, 'testimonial.html')
