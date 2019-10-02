from django.contrib import admin
from .models import MpesaPayment, User, Bills

admin.site.register(MpesaPayment)
admin.site.register(User)
admin.site.register(Bills)
