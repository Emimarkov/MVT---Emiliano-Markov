from django.shortcuts import render
from .models import Family

def datos(request):
    familys= Family.objects.all()
    context= {'family':familys}
    return render(request,'index.html',context)
