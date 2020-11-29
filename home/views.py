from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import dtl
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"index.html")
 
def cal(request):
   
    return render(request,"cal.html")
def dtl(request):
    if request.method == "POST" :
        name= request.POST.get("name")
        phone = request.POST.get("phone")
        email= request.POST.get("email")
        desc = request.POST.get("desc")
        dtlt= dtl(name=name)
        dtlt.save()
    return render(request,"dtl.html")
