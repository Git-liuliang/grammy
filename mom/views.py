from django.shortcuts import render,redirect,HttpResponse
from mom import models
import json
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
        return render(request, "login.html",{"error":"用户名或密码错误！"})

def hosts(request):
    if request.method == "POST":
        num = int(request.POST.get("page_num"))
        print(num)
        v= models.Inventory.objects.all().order_by("-id")[5*num-1:5*num+4]
    else:
        v = models.Inventory.objects.all().order_by("-id")[0:5]
    return render(request,"hosts.html",{"host_list":v})




def rm(request,nid):
    models.Inventory.objects.filter(id=nid).delete()
    status = 1
    return HttpResponse(json.dumps({"status":status}))


def add(request):
    if request.method == "POST":
        v = request.POST
        mod_dict = {"host": v.get("host"), "department": v.get("department"),
                    "position": v.get("position"),"group_id": v.get("group_id")}
        print(mod_dict)
        models.Inventory.objects.create(**mod_dict)
        return redirect("/hosts/")

    group_list = models.Group.objects.all()

    return render(request, "add.html", locals())

def reg(request):
    if request.method == "POST":
        v = request.POST
        dupcate = models.Userinfo.objects.filter(email=v.get("email")).first()
        if dupcate:
            return render(request,"registry.html",{"error":"email已经被使用！"})
        else:
            user_dict = {"username":v.get("username"),"email":v.get("email"),"password":v.get("password")}
            models.Userinfo.objects.create(**user_dict)
            return render(request, "registry.html", {"error": "注册成功！"})
    else:
        return render(request,"registry.html")


def edit(request,nid):
    if request.method == "POST":

        v = request.POST
        mod_dict = {"host": v.get("host"), "department": v.get("department"),
                    "position": v.get("position"), "group_id": v.get("group_id")}
        print(mod_dict)
        models.Inventory.objects.filter(id=nid).update(**mod_dict)
        return redirect("/hosts/")


    edit_content = models.Inventory.objects.filter(id=nid).first()

    group_list = models.Group.objects.all()

    return render(request,"edit.html",locals())


