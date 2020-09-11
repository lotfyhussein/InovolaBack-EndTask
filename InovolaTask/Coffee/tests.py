from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from Coffee.models import CoffeeMachine, CoffeePod
from rest_framework import status
from django.test.testcases import SerializeMixin

User = get_user_model()


class TestCoffeeMachineAPI(TestCase):

    def setUp(self):
        # First we create a user object to use it to make requests. 
        self.user = User.objects.create_user(username='lotfy', email='lotfy@example.com', password='123456')
        self.client = Client()
        self.client.force_login(self.user)
    
        # Then we create 4 CoffeeMachine objects to use the for testing
        self.machine_1 = CoffeeMachine.objects.create(product_type='COFFEE_MACHINE_LARGE', water_line_compatible=False, model='BASE')
        self.machine_2 = CoffeeMachine.objects.create(product_type='COFFEE_MACHINE_SMALL', water_line_compatible=True, model='PREMIUM')
        self.machine_3 = CoffeeMachine.objects.create(product_type='ESPRESSO_MACHINE', water_line_compatible=True, model='DELUXE')
        self.machine_4 = CoffeeMachine.objects.create(product_type='ESPRESSO_MACHINE', water_line_compatible=False, model='BASE')

    def tearDown(self):
        self.user.delete()
        self.machine_1.delete()
        self.machine_2.delete()
        self.machine_3.delete()
        self.machine_4.delete()
    
    def test_getting_coffee_machine_by_id(self):

        # Here we call the endpoint to get only the first object
        resp = self.client.get('/api/coffeemachine/1/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Make sure only the first object is returned
        self.assertEqual(resp.data['id'], 1)

    def test_getting_coffee_machines_by_using_filters(self):

        # Here we call the endpoint to get only COFFEE_MACHINE_LARGE
        resp = self.client.get('/api/coffeemachine/?product_type=COFFEE_MACHINE_LARGE')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Make sure we only recieved one object since we have only on Large voffee machine
        self.assertEqual(len(resp.data), 1)

        # Then we call the endpoint to get the ones that are water_line_compatible
        resp = self.client.get('/api/coffeemachine/?water_line_compatible=True')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Make sure we recieved 2 objects (second and third machine)
        self.assertEqual(len(resp.data), 2)

        # Then we call the endpoint to get the ones that are espresso machine, not water_line_compatible, with a base model
        resp = self.client.get('/api/coffeemachine/?product_type=ESPRESSO_MACHINE&water_line_compatible=False&model=BASE')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Make sure we recieved 1 object (fourth machine)
        self.assertEqual(len(resp.data), 1)


class TestCoffeePodAPI(TestCase):

    def setUp(self):
        # First we create a user object to use it to make requests. 
        self.user = User.objects.create_user(username='lotfy', email='lotfy@example.com', password='123456')
        self.client = Client()
        self.client.force_login(self.user)
    
        # Then we create 4 CoffeePod objects to use the for testing
        self.pod_1 = CoffeePod.objects.create(product_type='COFFEE_POD_LARGE', coffee_flavor='COFFEE_FLAVOR_VANILLA', pack_size=1)
        self.pod_2 = CoffeePod.objects.create(product_type='COFFEE_POD_SMALL', coffee_flavor='COFFEE_FLAVOR_CARAMEL', pack_size=3)
        self.pod_3 = CoffeePod.objects.create(product_type='ESPRESSO_POD', coffee_flavor='COFFEE_FLAVOR_MOCHA', pack_size=4)
        self.pod_4 = CoffeePod.objects.create(product_type='ESPRESSO_POD', coffee_flavor='COFFEE_FLAVOR_PSL', pack_size=3)

    def tearDown(self):
        self.user.delete()
        self.pod_1.delete()
        self.pod_2.delete()
        self.pod_3.delete()
        self.pod_4.delete()
    
    def test_getting_coffee_pod_by_id(self):

        # Here we call the endpoint to get only the first object
        resp = self.client.get('/api/coffeepod/1/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Make sure only the first object is returned
        self.assertEqual(resp.data['id'], 1)

    def test_getting_coffee_pods_by_using_filters(self):

        # Here we call the endpoint to get only COFFEE_POD_LARGE
        resp = self.client.get('/api/coffeepod/?product_type=COFFEE_POD_LARGE')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Make sure we only recieved one object since we have only one Large coffee pod
        self.assertEqual(len(resp.data), 1)

        # Then we call the endpoint to get the ones that are have MOCHA flavor
        resp = self.client.get('/api/coffeepod/?coffee_flavor=COFFEE_FLAVOR_MOCHA')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Make sure we recieved 1 object (third pod)
        self.assertEqual(len(resp.data), 1)

        # Then we call the endpoint to get the ones that are espresso pods, PSL flavor, with pack size 3
        resp = self.client.get('/api/coffeepod/?product_type=ESPRESSO_POD&coffee_flavor=COFFEE_FLAVOR_PSL&pack_size=3')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Make sure we recieved 1 object (fourth pod)
        self.assertEqual(len(resp.data), 1)
