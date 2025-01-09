from django.urls import path
from .views import create_user, update_user, read_user, listUsers, delete_user

urlpatterns = [
    path("users/", listUsers, name="listUsers"),
    path("users/create/", create_user, name="create"),
    path("users/<str:user_id>/", read_user, name="read"),
    path("users/<str:user_id>/update/", update_user, name="update"),
    path("users/<str:user_id>/delete/", delete_user, name="delete"),
]
