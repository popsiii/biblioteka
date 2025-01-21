<<<<<<< HEAD
from django.urls import path
from . import views

=======

from django.urls import path
from .views import KsiazkaListCreate, KsiazkaDetail

urlpatterns = [
    path('ksiazki/', KsiazkaListCreate.as_view(), name='ksiazka-list-create'),
    path('ksiazki/<int:pk>/', KsiazkaDetail.as_view(), name='ksiazka-detail'),
]
>>>>>>> 31b6cf79c82ce6c9cc72082ffed60aeb00ee9db2
