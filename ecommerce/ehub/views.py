from django.shortcuts import render,redirect
from .models import Product
from django.views.decorators.csrf import csrf_exempt
cart=[]
total=0
from django.http import HttpResponse

def home(request):
    dests=Product.objects.all()
    return render(request,'index.html',context={'dests':dests})
@csrf_exempt
def search(request):
    if request.method=='POST':
        category=request.POST.get('category-name')
        queryset=Product.objects.filter(productcategory=category)
        if len(queryset)>0:
            return render(request,'search.html',context={'queryset':queryset})
        else:
            queryset=Product.objects.all()
            return render(request,'search.html',context={'x':"noresult"})
    

@csrf_exempt
def detail(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'detail.html',{'product':product})

@csrf_exempt
def addcart(request,pk):
    global cart,total
    #if request.method=='POST':
    product=Product.objects.get(id=pk)
    cart.append(product)
    total+=product.productprize
    print(cart)
    return redirect('cart')

def Kart(request):
    global cart,total
    cart_set=set(cart)
    return render(request,'cart.html',{'cart':cart_set,'toal':total})


def checkout(request,toal):
    return render(request,'checkout.html',context={'toal':toal})

