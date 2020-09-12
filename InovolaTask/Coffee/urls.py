from Coffee import views
from rest_framework.routers import DefaultRouter

coffee_router = DefaultRouter()
coffee_router.register(r'coffeemachine', views.CoffeeMachineViewSet, base_name='coffeemachine')
coffee_router.register(r'coffeepod', views.CoffeePodViewSet, base_name='coffeepod')
