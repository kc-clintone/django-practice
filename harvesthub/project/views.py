from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Crop
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
import sqlite3
from .forms import ContactForm

# Create your views here.
def harvesthub(request):
    query = request.GET.get('q', '')
    crops = Crop.objects.filter(name__icontains=query) if query else Crop.objects.all()
    return render(request, 'harvesthub.html', {'crops': crops, 'query': query})

def contact(request):
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('harvesthub')
    else:
        cform = ContactForm()
    return render(request, 'harvesthub.html', {'form': cform})
