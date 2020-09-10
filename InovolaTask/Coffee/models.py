from django.db import models
from model_utils import Choices
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CoffeeMachine(models.Model):
    """
        Stores CoffeeMachines objects
    """
    TYPES = Choices(
        ('COFFEE_MACHINE_LARGE', _('coffee_machine_large')),
        ('COFFEE_MACHINE_SMALL', _('coffee_machine_small')),
        ('ESPRESSO_MACHINE', _('espresso_machine')),
)
    MODELS = Choices(
        ('BASE', _('base')),
        ('PREMIUM', _('premium')),
        ('DELUXE', _('deluxe')),
)
    product_type = models.CharField(max_length=30, choices=TYPES)
    water_line_compatible = models.BooleanField(db_index=True)


class CoffeePod(models.Model):
    """
        Stores CoffePods objects
    """
    TYPES = Choices(
        ('COFFEE_POD_LARGE', _('coffee_pod_large')),
        ('COFFEE_POD_SMALL', _('coffee_pod_small')),
        ('ESPRESSO_POD', _('espresso_pod')),
)

    FLAVORS = Choices(
        ('COFFEE_FLAVOR_VANILLA', _('coffee_flavor_vanilla')),
        ('COFFEE_FLAVOR_CARAMEL', _('coffee_flavor__caramel')),
        ('COFFEE_FLAVOR_PSL', _('coffee_flavor__psl')),
        ('COFFEE_FLAVOR_MOCHA', _('coffee_flavor__mocha')),
        ('COFFEE_FLAVOR_HAZELNUT', _('coffee_flavor__hazelnut')),
)
    product_type = models.CharField(max_length=255, choices=TYPES)
    coffee_flavor = models.CharField(max_length=255, choices=FLAVORS)
    pack_size =  models.IntegerField(_('Size in dozen'))