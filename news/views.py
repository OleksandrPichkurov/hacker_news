from rest_framework import generics
from news.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post, Comment, Vote
from .serializers import CommentSerializer, PostSerializer, VoteSerializer


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = "post_id"
    queryset = Post.objects.all()


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(parent=None)
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = "comment_id"
    queryset = Comment.objects.all()


class VoteListCreate(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
