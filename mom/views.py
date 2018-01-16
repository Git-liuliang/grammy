from django.shortcuts import render,redirect,HttpResponse
from mom import models
# Create your views here.
def homepage(request):
    return render(request, "login.html")

def login(request):
    front_email = request.POST.get("email")
    front_password = request.POST.get("password")
    v =models.Userinfo.objects.filter(email=front_email,password=front_password).first()

    if v:
        return render(request, "index.html")

    else:
        return HttpResponse("aaaaaa")

# def index(request):
#     return render(request,"index.html")