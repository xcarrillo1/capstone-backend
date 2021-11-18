from django import forms
from .models import Venue, Seat

class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = ('name', 'location', 'indoor', 'outdoor', 'photo_url')

class SeatForm(forms.ModelForm):

    class Meta:
        model = Seat
        fields = ('slocation', 'rating', 'image_url', 'reviewer', 'description')