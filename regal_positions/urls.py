from django.urls import path
from . import views

urlpatterns = [
    path('', views.regal_position_list_create_view),
    path('<int:pk>/update/', views.regal_position_update_view),
    path('<int:pk>/delete/', views.regal_position_destroy_view),
    path('<int:pk>/', views.regal_position_detail_view)
]
