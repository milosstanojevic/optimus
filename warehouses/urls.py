from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouse_list_create_view),
    path('<int:pk>/update/', views.warehouse_update_view),
    path('<int:pk>/delete/', views.warehouse_destroy_view),
    path('<int:pk>/', views.warehouse_detail_view)
]