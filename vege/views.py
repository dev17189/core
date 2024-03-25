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

    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context={'Receipes':queryset}

    return render(request,'index.html',context)

def update_rec(request,id):
    query=Receipe.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        receipe_img=request.FILES['receipe_image']
        receipr_name=data.get('receipe_name')
        receipr_description=data.get('receipe_description')

        query.receipe_name=receipr_name
        query.receipe_description=receipr_description
        
        if receipe_img:
            query.receipe_image=receipe_img
        
        query.save()
    
        return redirect('/receipe')

    context={'receipe':query}
    return render(request,'update_rec.html',context)

def delete_rec(request,id):
    query=Receipe.objects.get(id=id)
    query.delete()
    return redirect('/receipes')