from django.contrib.auth.models import User
from news.models import Post, Comment, Vote
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializers = self.parent.parent.__class__(value, context=self.context)
        return serializers.data


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    child = RecursiveSerializer(many=True, read_only=True)

    class Meta:

        model = Comment
        fields = ["post", "author", "content", "parent", "creation_date", "child"]


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["title", "link", "creation_date", "author", "up_votes"]
        read_only_fields = ["up_vote"]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
