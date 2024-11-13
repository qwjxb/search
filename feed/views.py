from django.shortcuts import render
from rest_framework import generics,status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

class CommentListCreatAPIView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, post_id):
        """
        Get the list of answers for a specific question.
        """
        try:
            post = Post.objects.get(id=post_id)  # Fetch the question by its ID
        except Post.DoesNotExist:
            return Response({"detail": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

        comments = post.comments.all()  # Access the related answers
        serializer = CommentSerializer(comments, many=True)  # Serialize the answers
        return Response(serializer.data)  # Return serialized answers

    def post(self, request, post_id):
        """
        Post a new answer for a specific question.
        """
        try:
            post = Post.objects.get(id=post_id)  # Fetch the question
        except Post.DoesNotExist:
            return Response({"detail": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)  # Deserialize the incoming data
        if serializer.is_valid():
            serializer.save(post_id=post)  # Save the answer linked to the question
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created answer data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if any
