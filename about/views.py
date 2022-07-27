from django.shortcuts import render
from .models import *
from main.models import Footer_text, Testimionals,Number_form_text
from main.models import Site_logo
from contact.models import Contact_info
# Create your views here.




def about(request):
    site_logo = Site_logo.objects.last()
    about_us = About_us.objects.last()
    team_text = Team_text.objects.last()
    team = Team.objects.all()
    testimionals = Testimionals.objects.all()
    form_text = Number_form_text.objects.last()
    footer_text = Footer_text.objects.last()
    contact_info = Contact_info.objects.last()

    context = {
        'about_us': about_us,
        'team_text': team_text,
        'team': team,
        'testimionals': testimionals,
        'form_text': form_text,
        'site_logo': site_logo,
        'footer_text': footer_text,
        'contact_info': contact_info,
    }

    return render(request, 'about.html', context)
