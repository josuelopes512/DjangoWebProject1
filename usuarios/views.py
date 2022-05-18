from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate , login as login_auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        _, created = User.objects.get_or_create(
            username=username,
            email=email,
            password=senha,
        )
        if not created:
            return HttpResponse('user is exist')
        return HttpResponse(username)

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login_auth(request, user)
            return HttpResponse('Autenticated')
        return HttpResponse('username or password invalides or dont exists')

@login_required(login_url='/auth/login/')
def plataforma(request):
    return HttpResponse('plataforma')