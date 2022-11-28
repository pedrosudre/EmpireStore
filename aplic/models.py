from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Cargo(models.Model):
    OPCOES = (
        ('Gerente', 'Gerente'),
        ('Atendente', 'Atendente'),
        ('Faturista', 'Faturista')
    )
    cargo = models.CharField("Cargo", max_length=100, choices=OPCOES)
    
    def __str__(self):
        return str(self.cargo)


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    cargo = models.ForeignKey(Cargo, on_delete=models.DO_NOTHING)
    salario = models.DecimalField("salario", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return str(self.cargo)