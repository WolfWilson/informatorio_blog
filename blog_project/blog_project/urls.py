from django.contrib import admin
from django.urls import path
from blog import views  # Importar las vistas desde tu aplicación 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),          # Página principal (index)
    path('about/', views.about, name='about'),    # Página "Acerca de"
    path('contact/', views.contact, name='contact'),  # Página de contacto
    path('articles/', views.articles, name='articles'),  # Página de artículos
]


