from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index_show_departments"),
    path('create', views.create, name='create_new_department'),
    path('edit/<str:code>', views.edit, name="edit_department"),
    #path('edit/update/<str:code>', views.update, name="update_department"),
    path('delete/<str:code>', views.delete, name='delete_department'),
]