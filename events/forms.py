from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%d-%m-%Y'),
        input_formats=['%d-%m-%Y']
    )

    class Meta:
        model = Event
        fields = ['title', 'description', 'date']
