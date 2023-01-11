from django.urls import path
from . import views
from .custom_views.transportArticleView import transport_article_options_list_view

urlpatterns = [
    path('', views.transport_article_list_create_view),
    path('<int:pk>/update/', views.transport_article_update_view),
    path('<int:pk>/delete/', views.transport_article_destroy_view),
    path('<int:pk>/', views.transport_article_detail_view),
    path('options/', transport_article_options_list_view)
]
