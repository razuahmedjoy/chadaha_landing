from django.shortcuts import render

# Create your views here.
from .models import HomeBanner, Projects, DonationCategory, DonationCampaign, OurTeam

def home(request):
    context = {}
    context['sliders'] = HomeBanner.objects.all()
    context['projects'] = Projects.objects.all()
    context['donation_categories'] = DonationCategory.objects.all()
    
    context['donation_campaigns'] = DonationCampaign.objects.all()
    return render(request, 'home.html',context)


def about_us(request):
    context = {}
    return render(request, 'hello world',context)

def our_team(request):
    context = {}
    return render(request, 'hello world',context)