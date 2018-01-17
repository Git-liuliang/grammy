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

def hosts(request):
    v = models.Inventory.objects.all()
    print("aaaa")
    return render(request,"hosts.html",{"host_list":v})

def mod(request,nid):
    v = request.POST
    mod_dict = {"host":v.get("host"),"hostname":v.get("hostname"),"department":v.get("department"),"position":v.get("position"),"manager":v.get("manager")}
    print(mod_dict)
    models.Inventory.objects.filter(id=nid).update(**mod_dict)
    return redirect("/hosts/")
