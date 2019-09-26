from django.db import models




class Payment(models.Model):
    name = models.CharField(max_length = 65, blank=True)
    account = models.IntegerField(default=0)
    phone_Number= models.IntegerField(default=0)
    amount = models.IntegerField(default=0)


    def __str__(self):
        return self.name