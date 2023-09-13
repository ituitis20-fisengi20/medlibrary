from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from app.forms import CustomLoginForm, CustomPasswordChangeForm

urlpatterns = [
    path('',views.home, name='home'),
    path('anasayfa/',views.home, name='home'), 
    path('kayit_ol/',views.sign_up, name='sign_up'),
    path("sifre_degistir/", auth_views.PasswordChangeView.as_view(form_class = CustomPasswordChangeForm), name='password_change'),
    path("giris_yap/", auth_views.LoginView.as_view(authentication_form = CustomLoginForm), name='login'),
    path("cikis_yap/", auth_views.LogoutView.as_view(), name='logout'),
    path("sifre_sifirla/", auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('akademisyen_ara/',views.search_academician, name='searchAcademician'),
    path('akademisyen_ekle/', views.add_academician),
    path('ders_ekle/', views.add_lesson),
    path('ders_notlari/', views.lesson_notes),
    path('temp/', views.temp),
    
]
