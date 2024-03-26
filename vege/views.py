from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
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


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return render(request, 'login.html')

        else:
            user= authenticate(username=username,password=password)

            if user is None:
                messages.error(request, "Invalid password")
                return render(request, 'login.html')
            
            else:
                login(request,user)
                return redirect('/rec')
    return  render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "username already exists")
            return render(request,'register.html')

        user=User.objects.create(
            first_name=first_name,
            last_name=lastname,
            username=username,
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        return redirect('/login')
    return  render(request, 'register.html')