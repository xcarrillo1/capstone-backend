from rest_framework import serializers
from .models import Venue, Seat

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    seats = serializers.HyperlinkedRelatedField(
        view_name='seat_detail',
        many=True,
        read_only=True
    )

    venue_url = serializers.ModelSerializer.serializer_url_field(     view_name='venue_detail'
    )

    class Meta:
       model = Venue 
       fields = ('id', 'venue_url', 'name', 'location', 'indoor', 'outdoor', 'photo_url', 'seats',)

class SeatSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='seat_detail',
        read_only=True
    )

    venue_id = serializers.PrimaryKeyRelatedField(
    queryset=Venue.objects.all(),
    source='venue'
    )

    class Meta:
        model = Seat
        fields = ('id', 'venue', 'venue_id', 'slocation', 'rating', 'image_url', 'reviewer', 'description')