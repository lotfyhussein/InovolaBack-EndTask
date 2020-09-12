from django.contrib import admin
from Coffee.models import CoffeeMachine, CoffeePod


class CoffeeMachineAdmin(admin.ModelAdmin):
    """Admin View for model:`Coffee.CoffeeMachine`."""

    list_display = ['id', 'product_type', 'water_line_compatible']
    list_filter = ['product_type', 'water_line_compatible']


admin.site.register(CoffeeMachine, CoffeeMachineAdmin)


class CoffeePodAdmin(admin.ModelAdmin):
    """Admin View for model:`Coffee.CoffeeMachine`."""

    list_display = ['id', 'product_type', 'coffee_flavor', 'pack_size']
    list_filter = ['product_type', 'coffee_flavor', 'pack_size']


admin.site.register(CoffeePod, CoffeePodAdmin)
