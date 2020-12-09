from django.shortcuts import render,redirect
from .models import Product,fashion,test
from django.views.decorators.csrf import csrf_exempt
cart=[]
total=0
from django.http import HttpResponse

def productpage(request):
    mobiles=Product.objects.filter(productcategory='mobiles')
    fashion=Product.objects.filter(productcategory='fashion')
    household=Product.objects.filter(productcategory='household')
    sports=Product.objects.filter(productcategory='sports')
    accessories=Product.objects.filter(productcategory='accessories')
    gifts=Product.objects.filter(productcategory='gifts')
    hardware=Product.objects.filter(productcategory='hardware')
    beauty=Product.objects.filter(productcategory='beauty')
    decorative=Product.objects.filter(productcategory='decorative')
    stationary=Product.objects.filter(productcategory='sationary')
    context={'mobiles':mobiles,'fashion':fashion,'household':household,'sports':sports,'accessories':accessories,
            'gifts':gifts,'hardware':hardware,'beauty':beauty,'decorative':decorative,'stationary':stationary}
    return render(request,'productpage.html',context)
    #return render(request,'productpage.html')

def home(request):
    dests=Product.objects.all()
    return render(request,'index.html',context={'dests':dests})
@csrf_exempt
def search(request):
    if request.method=='POST':
        category=request.POST.get('category-name')
        queryset=fashion.objects.filter(productcategory = category)
        if len(queryset)>0:
            return render(request,'product.html',context={'products': queryset})
        else:
            queryset=Product.objects.all()
            return render(request,'product.html',context={'products': queryset})
def test(request):   
    if request.method=='POST':
        category=request.POST.get('category-name')
        queryset=test.objects.filter(productcategory = category)
        if len(queryset)>0:
            return render(request,'product.html',context={'products': queryset})
        else:
            queryset=Product.objects.all()
            return render(request,'product.html',context={'products': queryset})

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

def about(request):
    return render(request,'about.html',)

def remove(request,id):
    item=Product.objects.get(id=id)
    global cart,total
    total-=item.productprize
    cart.remove(item)
    return redirect('/cart')



