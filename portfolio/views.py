from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, ContactMessage


def home(request):
    projects = Project.objects.filter(featured=True)
    skills = Skill.objects.order_by('name')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Thanks! Your message has been sent.')
            return redirect('home')
        messages.error(request, 'Please fill in all fields correctly.')

    return render(request, 'home.html', {
        'projects': projects,
        'skills': skills,
    })
