from django.shortcuts import render

from .models import Produto
# Create your views here.

def ProdutosView(request):
    produtos_lista = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})
