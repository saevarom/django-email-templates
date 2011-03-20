This small module is inspired by my need for sending templated emails, with the 
option of attaching an HTML formatted alternative.

Installation
=============

Installing::

    easy_install django-email-templates

Example usage
==============

The following example demonstrates how to send a templated email, in this case
the user has submitted a contact form. The module will look for the templates 
contact.txt and contact.html which will serve as the plaintext and html alternative
of the email. The default location of the templates is a directory named *email_templates*.::

    from email_templates import send_templated_mail

    context = {
        'name': request.POST['name'],
        'email': request.POST['email'],
        'telephone': request.POST['phone'],
        'message': request.POST['message'],
    }

    success = send_templated_mail(
        'Contact form submission',
        None, 
        [a[1] for a in settings.ADMINS],
        'contact',
        context
    )

