from django.contrib import admin
from django.urls import path
from apps.produtos.views import ProdutoListView, ProdutoCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProdutoListView.as_view(), name ='produtos_Lista'),
    path('produto/add/', ProdutoCreateView.as_view(), name = 'produto_create'),
    
]
