from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index_show_employees"),
    path('create', views.create, name='create_new_employee'),
    path('edit/<str:code>', views.edit, name="edit_employee"),
    path('update/<str:code>', views.update, name="update_employee"),
    path('delete/<str:code>', views.delete, name='delete_employee'),
]