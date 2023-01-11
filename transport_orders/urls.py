from django.urls import path
from . import views

urlpatterns = [
    path('', views.transport_order_list_create_view),
    path('<int:pk>/update/', views.transport_order_update_view),
    path('<int:pk>/delete/', views.transport_order_destroy_view),
    path('<int:pk>/', views.transport_order_detail_view)
]
