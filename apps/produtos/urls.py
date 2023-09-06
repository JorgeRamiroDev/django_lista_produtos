from .views import *
from django.urls import path


urlpatterns = [
    		path('lista-produtos/', ProdutosView),]