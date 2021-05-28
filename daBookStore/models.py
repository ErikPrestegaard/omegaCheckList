from typing import Reversible
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#Stores the Base information for each checklist
class checkLists(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('checklistDetail', kwargs={'pk': self.pk})

class checklistValue(models.Model):
    item = models.CharField(max_length=64)
    isChecked = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)
    belongsTo = models.ForeignKey(checkLists, on_delete=models.CASCADE, blank=True, null=True)
    #Missing createdby to attribute variables

    def __str__(self):
        return self.item
