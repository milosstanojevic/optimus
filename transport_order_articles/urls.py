from django.urls import path
from . import views

urlpatterns = [
    path('', views.transport_order_article_list_create_view),
    path('<int:pk>/update/', views.transport_order_article_update_view),
    path('stock/<int:pk>/update/',
         views.transport_order_article_add_to_stock_view),
    path('<int:pk>/delete/', views.transport_order_article_destroy_view),
    path('<int:pk>/', views.transport_order_article_detail_view)
]
