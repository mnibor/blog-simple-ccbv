from django.urls import path
from .views import dates, HomeListView, PostDetailView, CategoryListView, AuthorListView, PostCreateView

urlpatterns = [
    # PAGINA DE INICIO
    path('', HomeListView.as_view(), name='home'),

    # Detalle del Post
    path('post/<pk>', PostDetailView.as_view(), name='post'),

    # Filtrado por Categoría
    path('category/', CategoryListView.as_view(), name='category'),

    # Filtrado por Author
    path('author/', AuthorListView.as_view(), name='author'),

    # FILTRADO POR FECHA
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),

    # Crear Post
    path('create/', PostCreateView.as_view(), name='create'),
]