from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class HomeBanner(models.Model):

    banner_image = models.ImageField(upload_to='home_banner', blank=True, null=True)
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True, default="#")
    def __str__(self):
        return f"Banner- {self.id}"
    
    def get_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        else:
            return 'https://via.placeholder.com/1200x400'



class Projects(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='projects', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return 'https://via.placeholder.com/300x300'

class DonationCategory(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class DonationCampaign(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='donation_campaign', blank=True, null=True)
    target_amount = models.IntegerField(blank=True, null=True)
    collected_amount = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(DonationCategory, on_delete=models.CASCADE, blank=True, null=True)
    donating_account_info = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def remaining_amount(self):
        amount = self.target_amount - self.collected_amount
        if amount >=0:
            return amount
        else:
            return 0
    def collected_percent(self):
        percent = (self.collected_amount / self.target_amount)*100
        return percent
            
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return 'https://via.placeholder.com/300x300'

class DonationImages(models.Model):
    image = models.ImageField(upload_to='donation_images', blank=True, null=True)
    donation_campaign = models.ForeignKey(DonationCampaign, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return 'https://via.placeholder.com/300x300'


class TeamCategory(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OurTeam(models.Model):
    class Meta:
        ordering = ['serial_no']

    name = models.CharField(max_length=100, blank=True, null=True)
    team_category = models.ForeignKey(TeamCategory, on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='our_team', blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    whatsapp = models.CharField(max_length=13, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    linkedin_link = models.URLField(max_length=200, blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return "{% static 'images/placeholder.jpeg' %}"


class DonationRequest(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    contact_no = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='gallery', blank=True, null=True)
    is_video = models.BooleanField(default=False)
    video_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
    def gallery_image(self):
        if self.image:
            return self.image.url
        else:
            return 'https://via.placeholder.com/300x300'

    def get_video_id(self):
        if self.is_video:
            return self.video_link.split("=")[1]
        else:
            return None
    

class WebSettings(models.Model):
    donation_terms = RichTextField(blank=True, null=True)
    home_headline = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Web Settings"
    def __str__(self):
        return f"Web Settings-Never Delete"