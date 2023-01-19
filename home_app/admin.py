from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(HomeBanner)
admin.site.register(Projects)
admin.site.register(DonationCategory)

class DonationImageInline(admin.TabularInline):
    model = DonationImages
    extra = 3

class DonationAdmin(admin.ModelAdmin):
    list_display = ('title', 'target_amount', 'collected_amount', 'category')
    list_editable = ('target_amount', 'collected_amount', 'category')
    inlines = [DonationImageInline]

admin.site.register(DonationCampaign,DonationAdmin)

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image')
 
admin.site.register(OurTeam,OurTeamAdmin)
