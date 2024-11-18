from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Clubs
from .serializers import ClubSerializer
from .utils import get_available_id
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated



class ClubList(generics.ListCreateAPIView):
    queryset = Clubs.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        if not serializer.validated_data.get('id'):
            serializer.validated_data['id'] = get_available_id()
        serializer.save()
        
class ClubList(generics.ListCreateAPIView):
    queryset = Clubs.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        if not serializer.validated_data.get('id'):
            serializer.validated_data['id'] = get_available_id()
        serializer.save()

class ClubDetail(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request, club_id):
        try:
            club = Clubs.objects.get(id=club_id)
        except Clubs.DoesNotExist:
            return Response({"detail": "Club not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClubSerializer(club)
        return Response(serializer.data)

    def post(self, request, club_id):
        if not request.user.is_staff: 
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        try:
            club = Clubs.objects.get(id=club_id)
        except Clubs.DoesNotExist:
            return Response({"detail": "Club not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClubSerializer(club, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, club_id):
        if not request.user.is_staff: 
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        try:
            club = Clubs.objects.get(id=club_id)
        except Clubs.DoesNotExist:
            return Response({"detail": "Club not found."}, status=status.HTTP_404_NOT_FOUND)
        
        club.delete()
        return Response({"detail": "Club deleted successfully."}, status=status.HTTP_204_NO_CONTENT)