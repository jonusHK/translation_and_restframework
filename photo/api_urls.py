from django.urls import path
from .views import *

urlpatterns = [
    path('list/', PhotoListAPI.as_view()),
    path('create/', PhotoCreateAPI.as_view()),
    path('detail/<int:pk>/', PhotoDetailAPI.as_view()),
    path('update/<int:pk>/', PhotoUpdateAPI.as_view()),
    path('delete/<int:pk>/', PhotoDeleteAPI.as_view()),
]