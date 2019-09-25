from django.test import TestCase
from .models import User


# Create your tests here.
class Test_profile(TestCase):
    def setup(self):
        self.user=(id=1,username='peter',account_number='12345678',password='ppppppp'
        self.user.save()

        