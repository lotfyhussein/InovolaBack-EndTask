from django.db import models
from model_utils import Choices
from django.utils.translation import ugettext_lazy as _


class CoffeeMachine(models.Model):
    """
        Stores CoffeeMachines objects
    """
    TYPES = Choices(
        ('COFFEE_MACHINE_LARGE'),
        ('COFFEE_MACHINE_SMALL'),
        ('ESPRESSO_MACHINE'),
    )
    MODELS = Choices(
        ('BASE'),
        ('PREMIUM'),
        ('DELUXE'),
    )
    product_type = models.CharField(max_length=255, choices=TYPES, default=None)
    water_line_compatible = models.BooleanField(db_index=True, default=None)
    model = models.CharField(max_length=255, choices=MODELS, default=None)


class CoffeePod(models.Model):
    """
        Stores CoffePods objects
    """
    TYPES = Choices(
        ('COFFEE_POD_LARGE'),
        ('COFFEE_POD_SMALL'),
        ('ESPRESSO_POD'),
    )

    FLAVORS = Choices(
        ('COFFEE_FLAVOR_VANILLA'),
        ('COFFEE_FLAVOR_CARAMEL'),
        ('COFFEE_FLAVOR_PSL'),
        ('COFFEE_FLAVOR_MOCHA'),
        ('COFFEE_FLAVOR_HAZELNUT'),
    )
    product_type = models.CharField(max_length=255, choices=TYPES)
    coffee_flavor = models.CharField(max_length=255, choices=FLAVORS)
    pack_size = models.IntegerField(_('Size in dozen'))
