from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from events.models import Event, EventRegistration
from .forms import EventRegistrationForm
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request, 'home.html')

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

@login_required
def register(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            event_registration = form.save(commit=False)
            event_registration.user = request.user
            event_registration.save()
            messages.success(request, f"You have successfully registered for this event!")
            return redirect('events')
    else:
        form = EventRegistrationForm()

    return render(request, 'register.html', {'form': form})

def mylogout(request):
    logout(request)
    return redirect('/')

@login_required
def user_events(request):
    user_events = request.user.registered_events.all()
    return render(request, 'myevents.html', {'user_events': user_events})

@login_required
def cancel_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.registered_users.remove(request.user)
    return redirect('myevents')
