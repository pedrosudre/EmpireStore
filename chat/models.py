from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

class Message(models.Model):
    name = models.ForeignKey(Room, on_delete=models.CASCADE, null = True, blank = True)
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'


