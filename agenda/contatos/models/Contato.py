from contatos.models import *


class Contato(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.id} - {self.nome}'