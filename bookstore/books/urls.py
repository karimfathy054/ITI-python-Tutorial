from books import views
from django.urls import path

app_name = "books"
urlpatterns = [
    path("",views.index, name="index"),
    path("create",views.create, name="create"),
    path("store",views.store, name="store"),
    path("show/<int:id>",views.show, name="show"),
    path("edit/<int:id>",views.edit, name="edit"),
    path("update/<int:id>",views.update, name="update"),
    path("delete/<int:id>",views.delete, name="delete")
]
