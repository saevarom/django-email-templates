from django import forms
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from email_templates import send_templated_mail

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    message = forms.CharField(max_length=255, widget=forms.Textarea)

def contact(request):

    success = 0

    if request.method == 'POST':

        context = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }

        success = send_templated_mail(
            'Contact form was submitted', 
            None, # Uses the default FROM email of the project
            [a[1] for a in settings.ADMINS], # Send to all admins
            'contact', 
            context
        )

    form = ContactForm().as_p()

    d = {
        'form': form,
        'success': success,
    }

    return render_to_response('contact_form.html', d,
                              context_instance=RequestContext(request))
