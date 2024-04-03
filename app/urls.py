from django.urls import path
from .views import home, adding, update, delete

urlpatterns = [
    path('', home),
    path('add/', adding, name='add_task'),
    path('update/<int:task_id>/', update, name='update_task'),
    path('delete/<int:task_id>/', delete, name='delete_task'),
]