from django.urls import path

from library.api.users.views import (
    UserListView,
    UserDetailView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
)

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/update/", UserUpdateView.as_view(), name="user-update"),
    path("users/delete/", UserDeleteView.as_view(), name="user-delete"),
]

app_name = "library.api.users"
