from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")
def cal(request):
    return render(request,"cal.html")
def result(request):
    value_a = request.POST["valueA"]
    value_b = request.POST["valueB"]
    result= int(value_a)+int(value_b)
    #print(value_a,value_b,result)
    return render(request, "result.html", context={"result_resultHTML":result})
