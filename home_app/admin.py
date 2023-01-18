from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(HomeBanner)
admin.site.register(Projects)
admin.site.register(DonationCategory)
admin.site.register(DonationCampaign)

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image')
 
admin.site.register(OurTeam,OurTeamAdmin)
