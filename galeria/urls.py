from django.urls import path
from galeria.views import index, imagem

# ao criar o arquivo urls.py dentro do app, eu tiro a responsabilidade 
# do arquivo urls.py do setup de carregar os caminhos

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')

]