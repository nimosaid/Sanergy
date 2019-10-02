from rest_framework import serializers
from .models import *

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields='__all__'
