import profile
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KsiazkaViewSet, WypozyczeniaViewSet, HistoriaWypozyczenViewSet, SignUpView, home, profile
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'ksiazki', KsiazkaViewSet, basename='ksiazki')
router.register(r'wypozyczenia', WypozyczeniaViewSet, basename='wypozyczenia')
router.register(r'historia-wypozyczen', HistoriaWypozyczenViewSet, basename='historia-wypozyczen')

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'), 
    path('profile/', profile, name='profile') ,
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]

