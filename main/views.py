from django.shortcuts import redirect, render

from contact.models import Contact_info
from .models import About, Banner, Bot_token, Center_package, Chat_id, Feauters, Feedbacks, Footer_text, Intro_video, Left_package, Number_form_text, Packages_text, Right_package, Services, Services_text, Site_logo, Testimionals, Testimionals_text
import requests

# Create your views here.



def index(request):
    site_logo = Site_logo.objects.last()
    banner = Banner.objects.last()
    feauters = Feauters.objects.last()
    testimionals = Testimionals.objects.all()
    about = About.objects.last()
    intro_video = Intro_video.objects.last()
    services_text = Services_text.objects.last()
    services = Services.objects.all()
    testimionals_text = Testimionals_text.objects.last()
    feedbacks = Feedbacks.objects.all()
    paccages_text = Packages_text.objects.last()
    left_package = Left_package.objects.last()
    center_package = Center_package.objects.last()
    right_package = Right_package.objects.last()
    number_form_text = Number_form_text.objects.last()
    footer_text = Footer_text.objects.last()
    contact_info = Contact_info.objects.last()

    context = {
        'site_logo': site_logo,
        'banner': banner,
        'feauters': feauters,
        'testimionals': testimionals,
        'about': about,
        'intro_video': intro_video,
        'services_text': services_text,
        'services': services,
        'testimionals_text': testimionals_text,
        'feedbacks': feedbacks,
        'paccages_text': paccages_text,
        'left_package': left_package,
        'center_package': center_package,
        'right_package': right_package,
        'number_form_text': number_form_text,
        'footer_text': footer_text,
        'contact_info': contact_info,
    }
    return render(request, 'index.html', context)









def send_msg(request):
    botToken = Bot_token.objects.last().token
    if request.method == 'POST':
        phone = request.POST.get('text')
        text = 'Xabar\nTelefon raqam : ' + phone
        url = f'https://api.telegram.org/bot{botToken}/sendMessage?chat_id='
        chat_id = Chat_id.objects.all()
        for id in chat_id:
            requests.get(url+str(id.chat_id)+'&text='+text)
        return redirect(request.META.get('HTTP_REFERER'))
        
