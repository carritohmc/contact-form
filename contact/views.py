from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

def index(request):

    if request.method== 'POST':
        form = ContactForm(request.POST)

        # if it is valid, we will send the email
        if form.is_valid():
            print('It is valid, my friend')

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            # Use the template for testing emails

            # html =  render_to_string('contact/emails/contactform.html', {
            #     'name' : name,
            #     'email' : email,
            #     'content' : content

            # })

            # send_mail('The Subject', 'The Message', 'from@email.com', ['to@email.com'], html_message=html)

            # sending emails through gmail
            send_mail(
                f"Contact Form Submission: {subject}",
                f"Name: {name}\nEmail: {email}\n\nMessage:\n{content}",
                email,
                ['carritohmc@gmail.com'],
                fail_silently=False,
            )
            
            return redirect('index')
        # if we do not get any post requests, we just create a form instance
        # to render to the index.html
        else:
            form = ContactForm()

    form = ContactForm()

    return render(request, 'contact/index.html', {
        'form' :form
    })