from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.VenueList.as_view(), name='venue_list'),
    path('venues/', views.VenueList.as_view(), name='venue_list'),
    path('venues/<int:pk>', views.VenueDetail.as_view(), name='venue_detail'),
    path('seats/', views.SeatList.as_view(), name='seat_list'),
    path('seats/<int:pk>', views.SeatDetail.as_view(), name='seat_detail'),
]

#  FROM TEMPLATE (1-3 MARKDOWNS)
# urlpatterns = [
#     path('', views.venue_list, name='venue_list'),
#     path('seats/', views.seat_list, name='seat_list'),
#     path('venues/<int:pk>', views.venue_detail, name='venue_detail'),
#     path('seats/<int:pk>', views.seat_detail, name='seat_detail'),
#     path('venues/new', views.venue_create, name='venue_create'),
#     path('seats/new', views.seat_create, name='seat_create'),
#     path('venues/<int:pk>/edit', views.venue_edit, name='venue_edit'),
#     path('seats/<int:pk>/edit', views.seat_edit, name='seat_edit'),
#     path('venues/<int:pk>/delete', views.venue_delete, name='venue_delete'),
#     path('seats/<int:pk>/delete', views.seat_delete, name='seat_delete')
# ]