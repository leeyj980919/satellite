from django.shortcuts import redirect
from django.http import request

def index(request):
    return redirect("ocean/") 
    