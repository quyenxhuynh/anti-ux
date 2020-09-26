from django.shortcuts import render, redirect

def start(request):
    return render(request, 'anti_app/base.html')

def page1(request):
    return render(request, 'anti_app/create.html')