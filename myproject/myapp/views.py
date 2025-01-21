<<<<<<< HEAD
=======
from rest_framework import generics
from .models import Ksiazka
from .serializers import KsiazkaSerializer

class KsiazkaListCreate(generics.ListCreateAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer

class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
>>>>>>> 31b6cf79c82ce6c9cc72082ffed60aeb00ee9db2
