from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from Coffee.models import CoffeeMachine, CoffeePod
from Coffee.serializers import CoffeeMachineSerializer, CoffeePodSerializer


class CoffeeMachineViewSet(ModelViewSet):
    """
        Coffee Machines Endpoint.
        This API supports the following methods:

        GET: returns a single object if an id is provided or a list otherwise, according to the given filters.
        POST: adds a new object
        PUT: updates an object with an id provided
        DELETE: deletes an object

    """

    serializer_class = CoffeeMachineSerializer

    # Allow filtering the queryset by all fields
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'product_type', 'model', 'water_line_compatible']

    def get_queryset(self):
        return CoffeeMachine.objects.all()


class CoffeePodViewSet(ModelViewSet):
    """
        Coffee Pods Endpoint.
        This API supports the following methods:

        GET: returns a single object if an id is provided or a list otherwise, according to the given filters.
        POST: adds a new object
        PUT: updates an object with an id provided
        DELETE: deletes an object

    """

    serializer_class = CoffeePodSerializer

    # Allow filtering the queryset by all fields
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'product_type', 'coffee_flavor', 'pack_size']

    def get_queryset(self):
        return CoffeePod.objects.all()
