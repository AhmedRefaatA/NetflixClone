from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('show/<int:id>',views.show, name="show"),
    path('edite/<int:id>',views.edite, name="edite"),
    path('delete/<int:id>',views.delete, name="delete"),
]