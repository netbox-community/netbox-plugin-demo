from django.db import models
from netbox.models import NetBoxModel

class AccessList(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class AccessListRule(NetBoxModel):
    access_list = models.ForeignKey(AccessList, on_delete=models.CASCADE, related_name='rules')
    sequence = models.PositiveIntegerField()
    action = models.CharField(max_length=50, choices=(('permit', 'Permit'), ('deny', 'Deny')))

    def __str__(self):
        return f"{self.access_list.name} - {self.sequence}"
