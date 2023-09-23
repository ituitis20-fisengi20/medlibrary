from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from app.models import *
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    
    return render(request,'app/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('/anasayfa')

    else:

        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form":form})

@login_required
def add_academician(request):
    if request.method == 'POST':
        form = AcademicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/anasayfa')
        else:
            print("not okay")
    else:

        form = AcademicianForm()

    return render(request, 'app/addAcademician.html',{"form":form})

@login_required
def search_academician(request):
    form = SearchAcademicianForm()
    academicians = Academician.objects.all()

    if request.method == 'POST':
        form = SearchAcademicianForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            academicians = Academician.objects.filter(name__icontains = search_query)

    return render(request, 'app/searchAcademician.html',{'form':form, 'academicians':academicians})

@login_required
def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/anasayfa')
        else:
            print("not okay")
    else:

        form = LessonForm()

    return render(request, 'app/addAcademician.html',{"form":form})


def temp(request):
    form = tempform()
    return render(request, 'app/temp.html',{"form":form})

def lesson_notes(request):

    if request.method == 'POST':
        form = SearchLessonForm(request.POST)
        
        if form.is_valid():
            selected_lesson = request.POST.get('search_query_lesson', '')
            selected_copy_or_note = request.POST.get('search_query_copy_or_note', '')
            lessons = Lesson.objects.filter(name=selected_lesson, copy_or_note= selected_copy_or_note).order_by('lesson_year')
            
    else:
        form = SearchLessonForm()
        lessons = Lesson.objects.all().order_by('-lesson_year')

    paginator = Paginator(lessons,10)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the courses for the current page
    lessons = paginator.get_page(page_number)
        
    return render(request, 'app/lessonsNote.html',{'form':form, 'lessons':lessons})