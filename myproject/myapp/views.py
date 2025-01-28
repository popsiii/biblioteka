from rest_framework import generics, viewsets, status
from .models import Ksiazka, Uzytkownik, Wypozyczenia, HistoriaWypozyczen
from .serializers import KsiazkaSerializer, WypozyczeniaSerializer, HistoriaWypozyczenSerializer
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm



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


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home(request):
    return render(request, 'home.html') 


@login_required
def profile(request):
    return render(request, 'myapp/profile.html')

@login_required
def wypozycz_ksiazke(request):
    query = request.GET.get('q')
    if query:
        ksiazki = Ksiazka.objects.filter(tytul__icontains=query)  # Dopasowanie po tytule
    else:
        ksiazki = Ksiazka.objects.all()
    return render(request, 'myapp/wypozycz_ksiazke.html', {'ksiazki': ksiazki})

@login_required
def wypozycz(request, ksiazka_id):
    ksiazka = get_object_or_404(Ksiazka, id=ksiazka_id)
    Wypozyczenia.objects.create(uzytkownik=request.user, ksiazka=ksiazka)
    return redirect('profile')


@login_required
def zwroc_ksiazke(request, wypozyczenie_id):
    wypozyczenie = get_object_or_404(Wypozyczenia, id=wypozyczenie_id)
    wypozyczenie.zwroc_ksiazke()
    return redirect('profile')

# filepath: /Users/werus/biblioteka/myproject/myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Ksiazka, Wypozyczenia, HistoriaWypozyczen
from django.views.decorators.http import require_POST
from django.contrib.auth import logout

# filepath: /Users/werus/biblioteka/myproject/myapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wypozyczenia, HistoriaWypozyczen, Uzytkownik

@login_required
def profile(request):
    if request.user.is_staff:
        wypozyczenia = Wypozyczenia.objects.all()
        uzytkownicy = Uzytkownik.objects.all()
        ksiazki = Ksiazka.objects.all()
    else:
        wypozyczenia = Wypozyczenia.objects.filter(uzytkownik=request.user)
        uzytkownicy = None
        ksiazki = None
    historia_wypozyczen = HistoriaWypozyczen.objects.filter(uzytkownik=request.user)
    return render(request, 'myapp/profile.html', {
        'wypozyczenia': wypozyczenia,
        'historia_wypozyczen': historia_wypozyczen,
        'uzytkownicy': uzytkownicy, 
        'ksiazki': ksiazki
    })

@require_POST
@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')

def nasza_biblioteka(request):
    return render(request, 'myapp/nasza_biblioteka.html')

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ksiazka
from .forms import KsiazkaForm

def is_superuser(user):
    return user.is_superuser


@login_required
def home(request):
    ksiazki = Ksiazka.objects.all()
    return render(request, 'home.html', {'ksiazki': ksiazki})


@user_passes_test(is_superuser)
@login_required
def lista_ksiazek(request):
    query = request.GET.get('q')
    if query:
        ksiazki = Ksiazka.objects.filter(tytul__istartswith=query)
    else:
        ksiazki = Ksiazka.objects.all()
    return render(request, 'myapp/lista_ksiazek.html', {'ksiazki': ksiazki})

@user_passes_test(is_superuser)
@login_required
def dodaj_ksiazke(request):
    if request.method == 'POST':
        form = KsiazkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ksiazek')
    else:
        form = KsiazkaForm()
    return render(request, 'myapp/dodaj_ksiazke.html', {'form': form})

@user_passes_test(is_superuser)
@login_required
def edytuj_ksiazke(request, ksiazka_id):
    ksiazka = get_object_or_404(Ksiazka, id=ksiazka_id)
    if request.method == 'POST':
        form = KsiazkaForm(request.POST, instance=ksiazka)
        if form.is_valid():
            form.save()
            return redirect('lista_ksiazek')
    else:
        form = KsiazkaForm(instance=ksiazka)
    return render(request, 'myapp/edytuj_ksiazke.html', {'form': form})

@user_passes_test(is_superuser)
@login_required
def usun_ksiazke(request, ksiazka_id):
    ksiazka = get_object_or_404(Ksiazka, id=ksiazka_id)
    if request.method == 'POST':
        ksiazka.delete()
        return redirect('lista_ksiazek')
    return render(request, 'myapp/usun_ksiazke.html', {'ksiazka': ksiazka})