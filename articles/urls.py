from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_create_view),
    path('<int:pk>/update/', views.article_update_view),
    path('<int:pk>/delete/', views.article_destroy_view),
    path('<int:pk>/', views.article_detail_view)
]
