from django.urls import path
from .views import LivroList, LivroDetail, AutorList, AutorDetail, CategoriaList, CategoriaDetail

urlpatterns = [
    # Rotas para Livro
    path('livros/', LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),

    # Rotas para Autor
    path('autores/', AutorList.as_view(), name='autores-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),

    # Rotas para Categoria
    path('categorias/', CategoriaList.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
]
