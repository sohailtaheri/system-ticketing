from django.forms import ModelForm
from .models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        # fields = ['name', 'topic', 'description']
        fields = '__all__'

class CloseTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['comment']
        # fields = '__all__'


