from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1><center>Bienvenue sur le site de Romain GARRABOS</center></h1>
        <h2><center>Curriculum Vitae</center></h2>
        <p><center><img src="Capture.jpg" alt=""width="500" height="600"></center></p>
    """)