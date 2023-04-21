from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateTodoAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyTodoAPIView.as_view(), name='get_delete_update_movie'),
]