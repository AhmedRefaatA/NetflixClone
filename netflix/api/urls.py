from django.urls import path
from .views import index, create, UpdateMovie, DeleteMovie


urlpatterns = [
    path("", index),
    path("create", create),
    path("update/<int:pk>/", UpdateMovie.as_view()),
    path("delete/<int:pk>/", DeleteMovie.as_view())
]