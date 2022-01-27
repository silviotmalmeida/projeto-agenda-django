from django.db import models
from django.utils import timezone


# criando a model de Categoria
class Categoria(models.Model):

    # criando o atributo nome como texto com tamanho máximo de 255
    nome = models.CharField(max_length=255)

    # definindo qual atributo da model será exibido na área administrativa
    def __str__(self):
        return self.nome


# criando a model de Contato
class Contato(models.Model):

    # criando o atributo nome como texto com tamanho máximo de 255
    nome = models.CharField(max_length=255)

    # criando o atributo sobrenome como texto com tamanho máximo de 255, opcional
    sobrenome = models.CharField(max_length=255, blank=True)

    # criando o atributo telefone como texto com tamanho máximo de 255
    telefone = models.CharField(max_length=255)

    # criando o atributo email como texto com tamanho máximo de 255, opcional
    email = models.CharField(max_length=255, blank=True)

    # criando o atributo data_criacao como datetime atual
    data_criacao = models.DateTimeField(default=timezone.now)

    # criando o atributo descricao como texto, opcional
    descricao = models.TextField(blank=True)

    # criando o atributo categoria com referência à model Categoria, sem deleção em castaca
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    # criando o atributo descricao como booleano, com default True
    ativo = models.BooleanField(default=True)

    # criando o atributo foto, opcional, e definindo o destino do arquivo
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    # definindo qual atributo da model será exibido na área administrativa
    def __str__(self):
        return self.nome
