"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/warehouses/', include('warehouses.urls')),
    path('api/merchants/', include('merchants.urls')),
    path('api/articles/', include('articles.urls')),
    path('api/regals/', include('regals.urls')),
    path('api/regal-positions/', include('regal_positions.urls')),
    path('api/warehouse-articles/', include('warehouse_articles.urls')),
    path('api/merchant-articles/', include('merchant_articles.urls')),
    path('api/transports/', include('transports.urls')),
    path('api/transport-orders/', include('transport_orders.urls')),
    path('api/transport-order-articles/',
         include('transport_order_articles.urls')),
    path('api/transport-articles/', include('transport_articles.urls')),
]
