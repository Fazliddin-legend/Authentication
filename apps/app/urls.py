from django.urls import path
from .views import *


urlpatterns = [
    path('/items/create', ItemCreateView.as_view()),
    path('/items/action/<int:pk>', ItemUpdateDeleteView.as_view())
]
