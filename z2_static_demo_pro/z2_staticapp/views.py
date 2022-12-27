from django.shortcuts import render
from . models import Place
from . models import People

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1 = People.objects.all()
    return render(request,'index.html',{'result':obj , 'result1':obj1})
# def demo1(request):
#     obj1=People.objects.all()
#     return render(request, 'index.html', {'result1': obj1})
