from django.urls import path
from .views import ClubList, ClubDetail

urlpatterns = [
    path('clubs/', ClubList.as_view(), name='club_list'),
    path('clubs/<int:club_id>/', ClubDetail.as_view(), name='club_detail'),
]
