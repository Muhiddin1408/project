from django.shortcuts import render, redirect
from .models import *
from main.models import Bot_token, Chat_id, Site_logo
import requests
from main.models import Site_logo, Footer_text


# Create your views here.





def contact(request):
    info = Contact_info.objects.last()
    address = Address.objects.last()
    site_logo = Site_logo.objects.last()
    footer_text = Footer_text.objects.last()

    context = {
        'info': info,
        'address': address,
        'site_logo': site_logo,
        'footer_text': footer_text,
    }

    return render(request, 'contact.html', context)



def contact_msg(request):
    botToken = Bot_token.objects.last().token
    if request.method == 'POST':
        phone = request.POST.get('number')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        text = 'Bog\'lanish\nTelefon raqam : ' + phone + '\nIsmi: ' + name + '\nMavzu: ' + subject + '\nXabar: ' + message
        url = f'https://api.telegram.org/bot{botToken}/sendMessage?chat_id='
        chat_id = Chat_id.objects.all()
        for id in chat_id:
            requests.get(url+str(id.chat_id)+'&text='+text)
        return redirect('contact')
        
