from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data=request.POST
        receipe_img=request.FILES['receipe_image']
        receipr_name=data.get('receipe_name')
        receipr_description=data.get('receipe_description')
        
        Receipe.objects.create(receipe_name=receipr_name,receipe_description=receipr_description,receipe_image=receipe_img)
        return redirect('/receipes')


    queryset=Receipe.objects.all()
    context={'Receipes':queryset}

    return render(request,'index.html',context)

def delete_rec(request,id):
    query=Receipe.objects.get(id=id)
    query.delete()
    return redirect('/receipes')