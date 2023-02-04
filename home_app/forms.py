# create form for donationRequest model
from django import forms
from .models import DonationRequest

class DonationRequestForm(forms.ModelForm):


    def clean(self):
        # Get the user submitted names from the cleaned_data dictionary
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        amount = cleaned_data.get("amount")
        contact_no = cleaned_data.get("contact_no")
        address = cleaned_data.get("address")
     

        return cleaned_data
    class Meta:
        model = DonationRequest
        fields = ('__all__')
        labels = {
        "name":  "নাম",
        "amount": "পরিমান",
        "contact_no": "মোবাইল নম্বর",
        "address": "ঠিকানা",
    }
