from django.db import models

class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'e-mail de convidado'
        verbose_name_plural = 'e-mails de convidados'