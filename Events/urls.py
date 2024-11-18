from django.urls import path
from .views import EventList, EventDetail

urlpatterns = [
    path('events/', EventList.as_view(), name='event_list'),
    path('events/<int:event_id>/', EventDetail.as_view(), name='event_detail'),
]
