import os.path
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import AboutMe, Skill, Projects, ProjectsPage
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    if request.method == 'POST':
        message_subject = request.POST['message-subject']
        message_email = request.POST['message-email']
        message = request.POST['message']
        send_mail(message_subject, message, message_email, ['iwealadavid@gmail.com'] )

    about = AboutMe.objects.all()
    skill = Skill.objects.all()
    project = Projects.objects.all()
    form = ContactForm()
    context = {'about': about, 'skill': skill, 'project': project, 'form': form}
    return render(request, 'index.html', context)


def portfolio(request):
    about = AboutMe.objects.all()
    project = ProjectsPage.objects.all()
    context = {'about': about, 'project': project}
    return render(request, 'single.html', context)

def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response=HttpResponse(fh.read(), content_type="application/resume")
            response['Content-Disposition']='inline;filename'+os.path.basename(file_path)
            return response
        raise Http404

