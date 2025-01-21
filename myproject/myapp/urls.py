
from django.urls import path
from .views import KsiazkaListCreate, KsiazkaDetail

urlpatterns = [
    path('ksiazki/', KsiazkaListCreate.as_view(), name='ksiazka-list-create'),
    path('ksiazki/<int:pk>/', KsiazkaDetail.as_view(), name='ksiazka-detail'),
]