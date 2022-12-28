from django.urls import path
from .views import dates, HomeListView, PostDetailView, CategoryListView, AuthorListView, PostCreateView, PostUpdateView, PostDeleteView, AboutPageView

urlpatterns = [
    # PAGINA DE INICIO
    path('', HomeListView.as_view(), name='home'),

    # Detalle del Post
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),

    # Filtrado por Categoría
    path('category/', CategoryListView.as_view(), name='category'),

    # Filtrado por Author
    path('author/', AuthorListView.as_view(), name='author'),

    # Filtrado por Fecha
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),

    # Crear Post
    path('create/', PostCreateView.as_view(), name='create'),

    # Editar Post
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),

    # Eliminar Post
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),

    # About - Acerca de nosotros
    path('about/', AboutPageView.as_view(), name='about'),
]