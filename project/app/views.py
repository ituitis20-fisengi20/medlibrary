from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from app.models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def home(request):
    
    return render(request,'app/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Mark the user as inactive until email confirmation
            user.save()

            # Generate email confirmation token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Compose the email content
            subject = 'Confirm Your Email'
            message = render_to_string('email/confirmation_email.html', {
                'user': user,
                'token': token,
                'uid': uid,
            })
            plain_message = strip_tags(message)  # Strip HTML tags for plain text email

            # Send the confirmation email
            send_mail(subject, plain_message, 'alo145680@gmail.com', [user.email], html_message=message)

            # Redirect to a page informing the user to check their email for confirmation
            return render(request, 'registration/email_confirmation_required.html')

    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

def confirm_email(request, uidb64, token):
    try:
        # Decode the UID and get the user
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)

        # Check if the token is valid
        if default_token_generator.check_token(user, token):
            # Mark the user as active (confirmed)
            user.is_active = True
            user.save()

            # Optionally log in the user after confirmation
            # You can use the 'login' function here if you want

            # Redirect to a success page
            return render(request, 'registration/email_confirmation_success.html')

    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        pass

    # Redirect to a failure page or display an error message
    return HttpResponse('Email confirmation failed. Please contact support for assistance.')

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
            lessons = Lesson.objects
            if selected_lesson != 'any':
                lessons = lessons.filter(name=selected_lesson)
            lessons = lessons.filter(copy_or_note=selected_copy_or_note)
            lessons.order_by('lesson_year')
            
    else:
        form = SearchLessonForm()
        lessons = Lesson.objects.all().order_by('-lesson_year')

    paginator = Paginator(lessons,10)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the courses for the current page
    lessons = paginator.get_page(page_number)
        
    return render(request, 'app/lessonsNote.html',{'form':form, 'lessons':lessons})