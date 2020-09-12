from Coffee import views
from rest_framework.routers import DefaultRouter

coffee_router = DefaultRouter()
coffee_router.register(r'coffeemachine', views.CoffeeMachineViewSet, basename='coffeemachine')
coffee_router.register(r'coffeepod', views.CoffeePodViewSet, basename='coffeepod')
