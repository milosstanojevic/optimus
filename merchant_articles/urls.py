from django.urls import path
from . import views

urlpatterns = [
    path('', views.merchant_article_list_create_view),
    path('<int:pk>/update/', views.merchant_article_update_view),
    path('<int:pk>/delete/', views.merchant_article_destroy_view),
    path('<int:pk>/', views.merchant_article_detail_view)
]
