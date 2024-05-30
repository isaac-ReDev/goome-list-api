# from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class RestaurantTestCase(APITestCase):
    def um_e_um(self):
        self.assertEqual(1,3) 