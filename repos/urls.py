from django.urls import path
from repos import views

urlpatterns = [
    path('repos/', views.repo_list),
    path('repos/<int:pk>/', views.repo_detail),
]
