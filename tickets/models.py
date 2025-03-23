from django.db import models
from django import forms

from django.contrib.auth.models import User

class Ticket(models.Model):

    STATUS = ('open', 'Open'), ('complete', 'Complete'), ('done', 'Done'), ('abandoned', 'Abandoned')

    ticketId    = models.AutoField(primary_key=True)
    subject     = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    file        = models.FileField(upload_to='uploads/', null=True, blank=True)
    status      = models.CharField(max_length=50, default='Open', choices=STATUS)
    createdAt   = models.DateTimeField(auto_now_add=True)
    updatedAt   = models.DateTimeField(auto_now=True)
    user        = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    comment     = models.TextField(null=True, blank=True)

    class Meta:
        # puts the most recently created tickets at the top
        ordering = ['-createdAt', '-updatedAt']

    def __str__(self):
        return self.name