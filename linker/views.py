from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1><center>Bienvenue sur le site de Romain GARRABOS</center></h1>
        <h2><center>Curriculum Vitae</center></h2>
        <p><center><img src="../Capture.jpg" alt=""width="500" height="600"></center></p>
    """)

def date_actuelle(request):
    return render(request, 'linker/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
# Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'linker/addition.html', locals())