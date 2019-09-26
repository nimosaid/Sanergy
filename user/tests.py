from django.test import TestCase
from .models import Customer
from django.contrib.auth.models import User

# Create your tests here.
class Test_Profile(TestCase):
    def setup(self):
        self.user= Customer(id=1,phone_number='peter',account_number='12345678',password='ppppppp')
        self.user.save()

    def tearDown(self):
        Customer.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user,Customer))   
    