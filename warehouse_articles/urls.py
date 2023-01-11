from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouse_article_list_create_view),
    path('<int:pk>/update/', views.warehouse_article_update_view),
    path('<int:pk>/delete/', views.warehouse_article_destroy_view),
    path('<int:pk>/', views.warehouse_article_detail_view),
    path('query/', views.warehouse_article_detail_by_query_params_view)
]
