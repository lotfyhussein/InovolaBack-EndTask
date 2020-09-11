from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from Coffee.models import CoffeeMachine, CoffeePod
from Coffee.serializers import CoffeeMachineSerializer, CoffeePodSerializer
from rest_framework.response import Response
from rest_framework import status


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        coffee_machines = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(coffee_machines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(data='Object deleted successfully', status=status.HTTP_200_OK)


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        coffee_pods = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(coffee_pods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(data='Object deleted successfully', status=status.HTTP_200_OK)
