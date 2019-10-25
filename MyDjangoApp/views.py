from django.shortcuts import render
from MyDjangoApp.models import Tab
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")
def cal(request):
    return render(request,"cal.html")
def result(request):
    # if request.POST:
    if request.method=="POST":
        value_a = request.POST["valueA"]
        value_b = request.POST["valueB"]
        result= int(value_a)+int(value_b)
        print(value_a,value_b,result)
        Tab.objects.create(value_a=value_a,value_b=value_b,result=result)
        return render(request, "result.html", context={"result_Html":result})
    else:
        return HttpResponse("Please visit us with POST ...")

def list(request):
    list=Tab.objects.all()
    # for list in list
    #     print(list.value_a,list.value_b,list.result)
    return render(request, "list.html", context={"list_Html": list})
def delete(request):
    Tab.objects.all().delete()
    return HttpResponse("List deleted ...")



