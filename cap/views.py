# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from .models import Venue, Seat
# from .forms import VenueForm, SeatForm
from rest_framework import generics
from .serializers import VenueSerializer, SeatSerializer
from .models import Venue, Seat

class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class SeatList(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class SeatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

# Create your views here.
# def venue_list(request):
#     venues = Venue.objects.all()
#     return render(request, 'cap/venue_list.html', {'venues': venues})

# IF I WANT TO CREATE AN API
# def venue_list(request):
#     venues = Venue.objects.all().values('name', 'location', 'indoor', 'outdoor','photo_url') # only grab some attributes from our database, else we can't serialize it.
    # venues_list = list(venues) # convert our artists to a list instead of QuerySet
    # return JsonResponse(venues_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.

# def seat_list(request):
#     seats = Seat.objects.all()
#     return render(request, 'cap/seat_list.html', {'seats': seats})

# def venue_detail(request, pk):
#     venue = Venue.objects.get(id=pk)
#     return render(request, 'cap/venue_detail.html', {'venue': venue})

# def seat_detail(request, pk):
#     seat = Seat.objects.get(id=pk)
#     return render(request, 'cap/seat_detail.html', {'seat': seat})

# def venue_create(request):
#     if request.method == 'POST':
#         form = VenueForm(request.POST)
#         if form.is_valid():
#             venue = form.save()
#             return redirect('venue_detail', pk=venue.pk)
#     else:
#         form = VenueForm()
#     return render(request, 'cap/venue_form.html', {'form': form})

# def seat_create(request):
#     if request.method == 'POST':
#         form = SeatForm(request.POST)
#         if form.is_valid():
#             seat = form.save()
#             return redirect('seat_detail', pk=seat.pk)
#     else:
#         form = SeatForm()
#     return render(request, 'cap/seat_form.html', {'form': form})

# def venue_edit(request, pk):
#     venue = Venue.objects.get(pk=pk)
#     if request.method == "POST":
#         form = VenueForm(request.POST, instance=venue)
#         if form.is_valid():
#             venue = form.save()
#             return redirect('venue_detail', pk=venue.pk)
#     else:
#         form = VenueForm(instance=venue)
#     return render(request, 'cap/venue_form.html', {'form': form})

# def seat_edit(request, pk):
#     seat = Seat.objects.get(pk=pk)
#     if request.method == "POST":
#         form = SeatForm(request.POST, instance=seat)
#         if form.is_valid():
# 	        seat = form.save()
#         return redirect('seat_detail', pk=seat.pk)
#     else:
#         form = SeatForm(instance=seat)
#     return render(request, 'cap/seat_form.html', {'form': form})

# def venue_delete(request, pk):
#     Venue.objects.get(id=pk).delete()
#     return redirect('venue_list')

# def seat_delete(request, pk):
#     Seat.objects.get(id=pk).delete()
#     return redirect('seat_list')