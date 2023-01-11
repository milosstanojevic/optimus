from django.urls import path
from . import views

urlpatterns = [
    path('', views.transport_list_create_view),
    path('<int:pk>/update/', views.transport_update_view),
    path('<int:pk>/delete/', views.transport_destroy_view),
    path('<int:pk>/', views.transport_detail_view)
]
