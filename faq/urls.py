from django.urls import path
from . import views

urlpatterns = [
    # Autenticação
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
    # FAQ e Busca
    path('', views.HomeView.as_view(), name='home'),
    path('faq/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    
    # Perfil (Fluxo completo)
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/password/', views.CustomPasswordChangeView.as_view(), name='password_change'),
]