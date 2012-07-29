# views.py

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from contact.forms import ContactForm
from django.core.context_processors import csrf

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email', 'noreply@example.com'),
                    ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
            form = ContactForm()
    csrf_form = {'form': form}
    csrf_form.update(csrf(request))
    return render_to_response('contact_form.html', csrf_form) 
