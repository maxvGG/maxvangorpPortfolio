from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail
import re
# Create your views here.


def welcome(request):
    template = "welcome.html"
    context = {
        'template': template
    }
    return render(request, 'welcome.html', context)


def about(request):
    template = "about.html"
    context = {
        'template': template
    }
    return render(request, 'about.html', context)


def contact(request):
    template = "contact.html"
    context = {
        'template': template
    }
    return render(request, 'contact.html', context)


def sendEmail(request):
    if(checkmethod(request)):
        if checkemail(request.POST['email']):
            template = render_to_string('email_template.html', {
                'name': request.POST['name'],
                'email': request.POST['email'],
                'message': request.POST['message'],
            })
            send_mail(
                # subject
                request.POST['subject'],
                # email message
                template,
                # send mail to myself
                settings.EMAIL_HOST_USER,
                ['maxvangorp1001@gmail.com'],
                fail_silently=False,
            )
            return redirect('welcome')
        else:
            return HttpResponse('Please enter a valid Email')


# Make a regular expression
# for validating an Email
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def checkemail(email):
    if(re.search(regex, email)):
        return True
    else:
        return False


def checkmethod(request):
    if request.method == 'POST':
        return True
    else:
        return False
