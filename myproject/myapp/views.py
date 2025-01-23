from rest_framework import generics, viewsets, status
from .models import Ksiazka, Wypozyczenia, HistoriaWypozyczen
from .serializers import KsiazkaSerializer, WypozyczeniaSerializer, HistoriaWypozyczenSerializer
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class KsiazkaViewSet(viewsets.ModelViewSet):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer


class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer


class WypozyczeniaViewSet(viewsets.ModelViewSet):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.zwroc_ksiazke()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HistoriaWypozyczenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistoriaWypozyczen.objects.all()
    serializer_class = HistoriaWypozyczenSerializer