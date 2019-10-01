from rest_framework import serializers
from .models import *



class MpesaPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaPayment
        fields = ('reference', 'phone_numbaer', 'amount')