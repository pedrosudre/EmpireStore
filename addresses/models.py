from django.db import models
from billing.models import BillingProfile
from django.utils.translation import gettext_lazy as _


OPCOES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)
class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE, null = True, blank = True)
    address_type    = models.CharField(max_length = 120, choices = OPCOES)
    address_line_1  = models.CharField(_("Endereço 1"), max_length = 120)
    address_line_2  = models.CharField(_("Endereço 2"), max_length = 120, null = True, blank = True)
    city = models.CharField(_("Cidade"), max_length = 120)
    country = models.CharField(_("País"), max_length = 120, default = 'Brasil')
    state = models.CharField(_("Estado"), max_length = 120)
    postal_code = models.CharField(_("CEP"), max_length = 120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
                line1 = self.address_line_1,
                line2 = self.address_line_2 or "",
                city = self.city,
                state = self.state,
                postal= self.postal_code,
                country = self.country
            )
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
