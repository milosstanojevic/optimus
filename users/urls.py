from users.views import UserList, UserDetails, GroupList
from django.urls import path
from users.logged_user.views import get_user

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
    path('logged-user/', get_user),
]
