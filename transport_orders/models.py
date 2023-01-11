from django.db import models
from transports.models import Transport

# Create your models here.


class TransportOrder(models.Model):
    pending = '1'
    prepared = '2'
    taken = '3'
    in_transport = '4'
    arrived = '5'
    completed = '6'

    STATUS_CHOICES = [
        (pending, 'Pending'),
        (prepared, 'Prepared'),
        (taken, 'Taken'),
        (in_transport, 'In Transport'),
        (arrived, 'Arrived'),
        (completed, 'Completed'),
    ]

    parent = models.CharField(max_length=200)
    parent_id = models.PositiveBigIntegerField()
    transport = models.ForeignKey(
        Transport, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=pending)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
