from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Exam, StudentRegistration
from .forms import ExamForm, StudentRegistrationForm

# Exam CRUD views
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam_list.html', {'exams': exams})


def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'exam_form.html', {'form': form})


def exam_update(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm(instance=exam)
    return render(request, 'exam_form.html', {'form': form})


def exam_delete(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        exam.delete()
        return redirect('exam_list')
    return render(request, 'exam_confirm_delete.html', {'exam': exam})


# Student Registration views
@login_required
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.save()

            return redirect('exam_list')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_form.html', {'form': form})

@login_required
def my_exams(request):
    registrations = request.user.registrations.all()
    return render(request, 'my_exams.html', {'registrations': registrations})


# App views
def index(request):
    all_members = StudentRegistration.objects.all()
    return render(request,'index.html',{'all_members':all_members})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

#def register(request):
#    if request.method == "POST":
#        form = MemberForm(request.POST or None)
#        if form.is_valid():
#            form.save()
#       return render(request,'register.html',{})
#   else:
#
#     return render(request,'register.html', {})
