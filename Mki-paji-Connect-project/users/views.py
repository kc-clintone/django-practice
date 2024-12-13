from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request, 'form.html')

def edit(request):
    return render(request, 'edit.html')

