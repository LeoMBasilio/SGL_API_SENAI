from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    paginas = models.IntegerField()
    genero = models.CharField(max_length=100)
    ano_publicacao = models.DateField()

    def __str__(self):
        return self.titulo

class usuarios(models.Model):
    nome = models.CharField(max_length=100, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    celular = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)

    def __str__(self):
            return self.nome

class locacao(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    data_locacao = models.DateField(null=True, blank=True, auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    devolvido = models.BooleanField(null=True, blank=True)

    def __str__(self):
         return f'{self.usuario.nome} - {self.livro.titulo}'