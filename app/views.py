from django.shortcuts import render
from .data import get_images
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    return render(request,'index.html')

def products(request):
    images = get_images()
    return render(request, 'products.html',{'images':images})
def quality(request):
    return render(request, 'quality.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject= request.POST.get('subject')
        fax = request.POST.get('fax')
        phone = request.POST.get('phone')
        mobile_phone = request.POST.get('mobile_phone')
        website = request.POST.get('website')
        company = request.POST.get('company')
        send_mail(
            subject,
            f"""
            Konu: {subject}
            
            
            
            İsim Soyisim: {name}
            Email: {email}
            Faks: {fax}
            Telefon: {phone}
            Cep Telefonu: {mobile_phone}
            Web Sitesi: {website}
            Şirket: {company}
            """,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER]
        )
        return render(request, 'contact.html')
    return render(request, 'contact.html')

def production(request):
    return render(request,'production.html')

def about(request):
    return render(request,'about.html')

def vision(request):
    return render(request,'vision.html')

def bench(request):
    return render(request,'bench.html')