from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required # A pagina de membros so vai ser renderizada, quando o login for feito
def members (request):
    return render(request, 'members.html')