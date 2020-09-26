from django.shortcuts import render

def start(request):
    return render(request, 'anti_app/base.html')