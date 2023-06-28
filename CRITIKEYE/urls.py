"""
URL configuration for CRITIKEYE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from critikeye_app import views
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404
from critikeye_app.views import page_not_found

handler404 = page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('technophilesHome/', views.technophilesHome, name='technophilesHome'),
     path('technophiles/', views.technophiles, name='technophiles'),


    path('entreprises/', views.entreprises, name='entreprises'),

    path('fiche_produit/', views.create_product, name='fiche_produit'),

    path('logout/', views.user_logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('login/', views.user_login, name='user_login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('compte/', views.compte, name='compte'),

    path('create_accountTechnophiles/', views.creer_compte_technophile, name='create_accountTechnophiles'),
    path('create_accountEntreprises/', views.creer_compte_entrerpise, name='create_accountEntreprises'),
    
    path('cookie/preferences/', views.cookie_preferences, name='cookie_preferences'),
]
