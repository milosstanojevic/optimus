from django.urls import path
from . import views

urlpatterns = [
    path('', views.regal_list_create_view),
    path('<int:pk>/update/', views.regal_update_view),
    path('<int:pk>/delete/', views.regal_destroy_view),
    path('<int:pk>/', views.regal_detail_view)
]