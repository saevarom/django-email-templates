from django.core.mail import EmailMultiAlternatives, EmailMessage, get_connection
from django.template.loader import get_template
from django.template import Context, TemplateDoesNotExist

def send_templated_mail(subject, from_email, to, template_name, 
                        context={}, fail_silently=False, 
                        connection=None, template_prefix='email_templates/'):

    """
    A helper function which streamlines sending of templated 
    multipart/alternative e-mail messages.
    
    The function uses a connection if one is specified, otherwise the default 
    e-mail backend is used.
    
    The function looks for e-mail templates in the default directory 
    `email_templates/`. It is possible to override this by specifying a 
    different `template_prefix`. 
    
    It is possible to include both a text version of an e-mail and an html 
    version. It is highly recommended to include a text version is included 
    when sending an HTML formatted e-mail.
    
    The templates are loaded using this format:

        Plaintext: <template_prefix><template_name>.txt
        Multipart: <template_prefix>template_name>.html
    
    Using the default `template_prefix` and a `template_name` of 'welcome', 
    the function tries to load the following templates:
    
        email_templates/welcome.txt
        email_templates/welcome.html

    Finally, it is possible to provide a context dictionary which is passed 
    on to the template rendering.

    """

    connection = connection or get_connection(fail_silently=fail_silently)

    try:
        plaintext = get_template('%s%s.txt' % (template_prefix, template_name))
    except TemplateDoesNotExist:
        plaintext = None

    try:
        html = get_template('%s%s.html' % (template_prefix, template_name))
    except  TemplateDoesNotExist:
        html = None

    d = Context(context)

    text_content = plaintext.render(d) if plaintext else None
    html_content = html.render(d) if html else None

    result = 0

    if plaintext and html:
        print "plaintext and html"
        msg = EmailMultiAlternatives(subject, text_content, from_email, 
                                     to, connection=connection)
        msg.attach_alternative(html_content, "text/html")
        result = msg.send(fail_silently=fail_silently)

    if plaintext and not html:
        print "plaintext and not html"
        msg = EmailMessage(subject, text_content, from_email, to, 
                           connection=connection)
        result = msg.send(fail_silently=fail_silently)

    if html and not plaintext:
        print "html and not plaintext"
        msg=EmailMessage(subject, html_content, from_email, to, 
                         connection=connection)
        msg.content_subtype = 'html'
        result = msg.send(fail_silently)
    
    return result
