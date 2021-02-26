from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")

    def __str__(self) -> str:
        return self.title

    def up_votes(self):
        """Сounts the number of votes for a post"""
        return self.votes.all().count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    content = models.TextField(max_length=3000)
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, blank=True, null=True, related_name="child"
    )

    def __str__(self) -> str:
        return f"Comment by {self.author} on {self.post}"


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="votes")

    class Meta:
        unique_together = [("post", "voter")]

    def __str__(self) -> str:
        return f"{self.voter.username} upvoted {self.post.title}"
