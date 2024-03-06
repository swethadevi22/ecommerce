"""
URL configuration for ekart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),
    path("login/",auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',views.logout_page,name="logout"),
    path("register/",views.register,name='register'),
    path("collections/",views.collections,name='collections'),
    path("collections/<str:name>",views.collectionsview,name='collections'),
    path("collections/<str:cname>/<str:pname>",views.product_details,name='product_details'),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('cart/',views.cart_page,name="cart"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('checkout/',views.checkout,name="checkout"),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
