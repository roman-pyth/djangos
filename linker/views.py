from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.views.generic import *


def home(request):
    test={}
    """ HTML DANS CETTE FONCTION"""
    return render(request,'linker/home.html',test)

def date_actuelle(request):
    context = {'pseudo': 'Naveen', 'date': datetime.now(),
    'TEXTE1':"Les filtres permettent de modifier l’affichage en fonction d’une variable, sans passer par la vue. Prenons un exemple concret : sur la page d’accueil des sites d’actualités, le texte des dernières nouvelles est généralement tronqué, seul le début est affiché. Pour réaliser la même chose avec Django, nous pouvons utiliser un filtre qui limite l’affichage aux 80 premiers mots de notre article :"
    }
    return render(request, 'linker/date.html', context)

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
# Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'linker/addition.html', locals())
