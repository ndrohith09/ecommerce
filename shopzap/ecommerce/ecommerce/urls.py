"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from ehub import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>/',views.detail , name='detail'),
    path('search/',views.search,name='search'),
    path('add/<int:pk>',views.addcart,name='addtocart'),
    path('cart/',views.Kart,name='cart'),
    path('',views.home,name='home'),
    path('check/<toal>',views.checkout,name='checkput'),
    path('about/',views.about,name="about"),
    path('productpage/',views.productpage,name='productpage'),
    path('removeitemfromcart/<int:id>',views.remove,name='remove'),
   
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
