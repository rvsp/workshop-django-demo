from django.shortcuts import render

# Create your views here.
from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def contact_display(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['your_name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'venkatsubramanian707@gmail.com', [from_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "success.html")
    return render(request, "contact.html", {'form': form})
