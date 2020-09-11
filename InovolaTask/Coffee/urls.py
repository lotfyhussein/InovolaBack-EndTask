from Coffee import views
from rest_framework.routers import DefaultRouter

coffee_machines_router = DefaultRouter()
coffee_machines_router.register(r'coffeemachine',
                                views.CoffeeMachineViewSet,
                                base_name='coffeepod')
coffee_machines_router.register(r'coffeepod',
                                views.CoffeePodViewSet,
                                base_name='coffeepod')
