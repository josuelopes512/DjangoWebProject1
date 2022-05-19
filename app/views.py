"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import NewUserForm, UserClientForm
from .models import Vacancies, UserClient, Candidato



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Pagina Inicial',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contato',
            'message':'FastJobs Encontre já',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Sobre',
            'message':'No Fast Jobs você pode pesquisar milhões de vagas e decidir a trajetória da sua carreira.Temos ferramentas de busca, currículos e etc..',
            'year':datetime.now().year,
        }
    )

def vagas(request):
    """Renders the about page."""
    vagas = Vacancies.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vagas.html',
        {   
            'title':'Vagas Disponiveis',
            'vagas': vagas
        }
    )

def curriculo(request):
    form = UserClientForm()
    return render(
        request, 
        "app/curriculo.html",
        {
            'title':'Cadastro Curriculo',
            'form': form
        }
    )

def register_request(request):
	if(request.method == "POST"):
		form = NewUserForm(request.POST)
		if(form.is_valid()):
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(
        request, 
        "app/register.html",        
        {
            "title": "Registrar",
            "register_form":form
        }
    )

# class UserClientFormView(FormView):
#     form_class  = UserClientForm
#     success_url = reverse_lazy('success')
#     template_name = 'app/curriculo.html'