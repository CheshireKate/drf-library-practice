from django.urls import path

from library.api.users.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path("users/", UserListView.as_view(), basename="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), basename="user-detail"),
    path("users/create/", UserCreateView.as_view(), basename="user-create"),
    path("users/update/", UserUpdateView.as_view(), basename="user-update"),
    path("users/delete/", UserDeleteView.as_view(), basename="user-delete"),
]

app_name = "library.api.users"
