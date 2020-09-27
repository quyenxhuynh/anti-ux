from django.shortcuts import render, redirect
import time as t

t0 = None

def start(request):
    return render(request, 'anti_app/base.html')

def create(request):
    global t0
    t0 = t.time()
    return render(request, 'anti_app/create.html')

def time(request):
    global t0
    context = {'time':t.time() - t0}
    return render(request, 'anti_app/time.html', context)

def test(request):
    return render(request, 'anti_app/test.html')

def instructions(request):
    context = {}
    return render(request, 'anti_app/instructions.html', context)

def store(request):
    context = {}
    return render(request, 'anti_app/store.html', context)

def cart(request):
    context = {}
    return render(request, 'anti_app/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'anti_app/checkout.html', context)