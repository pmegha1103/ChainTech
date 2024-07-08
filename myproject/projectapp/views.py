from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from .models import FormSubmission

def index(request):
    current_datetime = datetime.now()
    context = {
        'current_datetime': current_datetime
    }
    return render(request, 'home.html', context)

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        submission = FormSubmission(name=name, email=email)
        submission.save()
        return redirect('form_submissions')
    return render(request, 'home.html')  

def form_submissions(request):
    submissions = FormSubmission.objects.all()
    return render(request, 'form_data.html', {'submissions': submissions})