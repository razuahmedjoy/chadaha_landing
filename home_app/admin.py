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
    list_display = ('name','team_category','serial_no')
    list_editable = ('team_category','serial_no')
    list_filter = ('team_category',)

 
admin.site.register(OurTeam,OurTeamAdmin)
admin.site.register(TeamCategory)
admin.site.register(WebSettings)

class galleryAdmin(admin.ModelAdmin):
    list_display = ('title','is_video','video_link')
    list_editable = ('is_video',)
    
admin.site.register(Gallery,galleryAdmin)

class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ('name','amount','contact_no','address','created_at')
    list_filter = ('created_at',)
admin.site.register(DonationRequest,DonationRequestAdmin)
