from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name="index"),
    path('update/<int:id>', views.update, name='update_task'),
    path('delete/<int:id>', views.delete, name='delete_task')
]