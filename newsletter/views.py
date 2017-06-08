from django.shortcuts import render,get_object_or_404
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from newsletter.models import SignUp
from django.contrib.auth.models import User


# Create your views here.

def home(request):

    my_title = "Welcome.."
    my_form = SignUpForm(request.POST or None)
    all_items = SignUp.objects.all()

    context = {
            'template_title': my_title,
            'my_form': my_form,
            'all_items': all_items,
    }

    if my_form.is_valid():
        all_items.delete()
        j = my_form.save(commit=False)
        j.save()
        context = {
                'template_title': 'Thank you',
        }
    return render(request, 'home.html', context)

def Contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')

        subject = 'This is the form email'
        from_email =  settings.EMAIL_HOST_USER
        to_email = [form_email]
        contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)

        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

    context = {
        'form': form,
        'template_title': 'Contact Us'
    }

    return render(request, 'contact.html', context)


def Profile(request):
    user = User.objects.all()
    all_items = SignUp.objects.all()
    return render(request, 'profile.html', {'all_items': all_items})

def wall(request, user_id):
    user = User.objects.all()
    all_items = SignUp.objects.all()
    person = get_object_or_404(user , id = user_id)
    settings.LOGIN_REDIRECT_URL = '/profile/'+str(user_id)+'/'
    return render(request, 'wall.html', {'all_items': all_items, 'user_id': user_id})

