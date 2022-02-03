from django.urls import path, include
from .views import *

urlpatterns = [
    path('', test, name='test'),
    path('rubric/<int:pk>', GetRubric.as_view(), name='rubric'),
]