from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm


def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('index')
