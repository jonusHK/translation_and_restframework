from django.urls import path
from .views import *

urlpatterns = [
    path('changelanguage/', change_language3, name='change_language'),
    path('sample/', sample),
    path('language/<code>/', change_language),
    path('', index),
]