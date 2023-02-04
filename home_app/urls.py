"""chadaha_landing_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.http import HttpResponse
from django.urls import path,include
from .views import *



urlpatterns = [
    path('', home, name='home'),   
    path('about-us/', about_us, name='about_us'),   
    path('our-team/', our_team, name='our_team'),   
    path('our-team/<int:pk>', our_team_single, name='our_team_single'),   
    path('donation/', all_donation, name='all_donation'),
    path('donation/<int:pk>/', single_donation, name='single_donation'),
    path('gallery/', gallery, name='gallery'),   
      
]

