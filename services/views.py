from django.shortcuts import render
from .models import *
from main.models import Footer_text, Site_logo
# Create your views here.





def services(request):
    services_text = Services_text.objects.last()
    services = Services.objects.all()
    explaining = Explaining.objects.last()
    services_introduction = Services_introduction.objects.last()
    site_logo = Site_logo.objects.last()
    footer_text = Footer_text.objects.last()
    
    context = {
        'services_text': services_text,
        'services': services,
        'explaining': explaining,
        'services_introduction': services_introduction,
        'site_logo': site_logo,
        'footer_text': footer_text,
    }

    return render(request, 'services.html', context)