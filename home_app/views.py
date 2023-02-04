from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse

# Create your views here.
from .models import *
from .forms import *
def home(request):
    context = {}
    context['sliders'] = HomeBanner.objects.all()
    context['projects'] = Projects.objects.all()
    context['donation_categories'] = DonationCategory.objects.all()
    context['websettings'] = WebSettings.objects.last()
    
    context['donation_campaigns'] = DonationCampaign.objects.all()
    return render(request, 'home.html',context)


def about_us(request):
    context = {}
    try:
        context['websettings'] = WebSettings.objects.last()
        return render(request, 'about.html',context)
    except:
        return redirect('home')
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

    if request.method == 'GET':
        try:
            context['donationForm'] = DonationRequestForm()
            context['donation'] = DonationCampaign.objects.get(id=pk)
            context['websettings'] = WebSettings.objects.last()
        except:
            return redirect("all_donation")
            
        
        return render(request, 'single_donation.html',context)
    elif request.method == 'POST':
        try:
            donation_request = DonationRequestForm(request.POST)
            if donation_request.is_valid():
                donation_request.save()
                return redirect(to='single_donation',pk=pk)
        except:
            return JsonResponse({'status':'error'})

def gallery(request):
    # contentType = request.GET.get()
    context = {}
    dataType = request.GET.get('type')

    if dataType != 'image' and dataType != 'video':
        return redirect('home')
    if dataType == 'image':
        context['gallery'] = Gallery.objects.filter(is_video=False)
        context['title'] = 'ছবিঘর'
    elif dataType == 'video':
        context['gallery'] = Gallery.objects.filter(is_video=True)
        context['title'] = 'ভিডিও'
    return render(request, 'gallery.html',context)

    # return JsonResponse({'contentType':type})