from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse("Welcome Home")

def viewAllNotes(request):
    today = datetime.today
    context = {"today" : today}
    return render(request, "home/welcome.html", context)

@login_required(login_url = "/admin")
def showAuthorized(request):
    context = {}
    return render(request, "home/authorized.html", context)
