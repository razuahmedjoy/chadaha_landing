from django.shortcuts import render, redirect

# Create your views here.
from .models import *

def home(request):
    context = {}
    context['sliders'] = HomeBanner.objects.all()
    context['projects'] = Projects.objects.all()
    context['donation_categories'] = DonationCategory.objects.all()
    
    context['donation_campaigns'] = DonationCampaign.objects.all()
    return render(request, 'home.html',context)


def about_us(request):
    context = {}
    return render(request, 'about.html',context)

def our_team(request):
    context = {}
    context['team_category'] = TeamCategory.objects.all()
    
    return render(request, 'our_team.html',context)

def our_team_single(request,pk):
    context = {}
    try:
        context['team_member'] = OurTeam.objects.get(id=pk)
    except:
        return redirect('our_team')
    
    return render(request, 'our_team_single.html',context)


def all_donation(request):
    context = {}
  
   
    context['donation_categories'] = DonationCategory.objects.all()

    return render(request, 'all_donation.html',context)

def single_donation(request,pk):
    context = {}
    try:
        context['donation'] = DonationCampaign.objects.get(id=pk)
        context['websettings'] = WebSettings.objects.last()
    except:
        return redirect("all_donation")
        
    
    return render(request, 'single_donation.html',context)