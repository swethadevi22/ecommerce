import json
from telnetlib import LOGOUT
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import *
def home(request):
       products=product.objects.filter(trending=1)
       return render(request,'home.html',{"products":products})
def login(request):
       return render(request,'login.html')
def collections(request):
       catagory=category.objects.filter(status=0)
       return render(request,'collections.html',{"category":catagory})
def collectionsview(request,name):
       if(category.objects.filter(name=name,status=0)):
              products=product.objects.filter(category__name=name)
              return render(request,'index.html/',{"products":products,"category":name})
       else:
              messages.warning(request,"No such category found")
              return redirect('collections')
def product_details(request,cname,pname):
       if(category.objects.filter(name=cname,status=0)):
              if(product.objects.filter(name=pname,status=0)):
                     products=product.objects.filter(name=pname,status=0).first()
                     return render(request,'product_details.html',{"products":products})
              else:
                     messages.error(request,'No such product found')
                     return redirect('collections')
       else:
              messages.error(request,'No such category found ')
              return redirect("collections")
def register(request):
       if request.method=='POST':
              form=UserRegistrationForm(request.POST)
              if form.is_valid():
                     form.save()
                     messages.success(request,'your account has beeen created')
                     return redirect('login')
       else:
              form=UserRegistrationForm()
       context={'form':form}
       return render(request,'register.html',context)

def add_to_cart(request):
       if request.headers.get('x-requested-with')=='XMLHttpRequest':
              if request.user.is_authenticated:
                     data=json.load(request)
                     product_qty=data['product_qty']
                     product_id=data['pid']
                     #print(request.user.id)
                     product_status=product.objects.get(id=product_id)
                     if product_status:
                            if Cart.objects.filter(user=request.user,product_id=product_id):
                                   return JsonResponse({'status':'Product Already in Cart'}, status=200)
                            else:
                                   if product_status.quantity>=product_qty:
                                          Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                                          return JsonResponse({'status':'Product Added to Cart'}, status=200)
                                   else:
                                          return JsonResponse({'status':'Product Stock Not Available'}, status=200)
              else:
                     return JsonResponse({'status':'Login to Add Cart'}, status=200)
       else:return JsonResponse({'status':'Invalid Access'}, status=200)
def cart_page(request):
  if request.user.is_authenticated:
    cart=Cart.objects.filter(user=request.user)
    return render(request,"cart.html",{"cart":cart})
  else:
    return redirect("/")
def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")
def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")
def checkout(request):
       return render(request,'check.html')