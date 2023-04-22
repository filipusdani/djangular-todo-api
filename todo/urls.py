from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateTodoAPIView.as_view(), name='get_post_todo'),
    path('<int:pk>/', views.RetrieveUpdateDestroyTodoAPIView.as_view(), name='get_delete_update_todo'),
    path('category/', views.ListCreateTodoCategoryAPIView.as_view(), name='get_post_todo_category'),
    path('category/<int:pk>/', views.RetrieveUpdateDestroyTodoCategoryAPIView.as_view(), name='get_delete_update_todo_category'),
]