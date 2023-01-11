from django.urls import path
from . import views

urlpatterns = [
    path('', views.merchant_list_create_view),
    path('<int:pk>/update/', views.merchant_update_view),
    path('<int:pk>/delete/', views.merchant_destroy_view),
    path('<int:pk>/', views.merchant_detail_view)
]
