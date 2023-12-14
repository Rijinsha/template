from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from.models import team
# Create your views here.

def demo(request):
    obj=place.objects.all()
    tm= team.objects.all()
    return render(request,"index.html",{'value':obj,'membrs':tm})
#def xyz(request):
  #  return render(request,"home.html")
#def passing(request):
 #def abc(request):
  #  return render(request,"psgone.html")
#def result(request):
##   y = int(request.GET['num2'])
#    res=x+y
#    return render(request,"results.html",{'result1' : res})