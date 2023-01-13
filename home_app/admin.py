from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(HomeBanner)
admin.site.register(Projects)
admin.site.register(DonationCategory)
admin.site.register(DonationCampaign)
admin.site.register(OurTeam)
